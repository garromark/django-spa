import base64
import hmac, hashlib
import time
from rest_framework.views import APIView
from rest_framework.response import Response
from spa.apps.api.permissions import IsStaff
from django.conf import settings

SUCCESS_ACTION_STATUS = 200

class S3Form(APIView):
    """
    Defines a GET view that will return the required Amazon S3 fields. These fields
    need to be bound to the form submitting the file to S3, otherwise AWS will not
    accept the file upload.
    """
    permission_classes = (IsStaff,)

    def get(self, request, format=None):
        folder = request.GET.get("folder", "")
        exp_d = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(time.time() + 600))
        policy_document = ('{"expiration": "' + exp_d + '",'
                           '"conditions": ['
                           '{"bucket": "' + settings.S3_BUCKET + '"},'
                           '{"success_action_status": "' + str(SUCCESS_ACTION_STATUS) + '"},'
                           '["starts-with", "$key", "' + folder + '"],'
                           '{"acl": "private"},'
                           '["starts-with", "$Content-Type", ""],'
                           '["content-length-range", 0, 1048576]  ]}')
        policy = base64.b64encode(policy_document)
        res = { 'policy': policy,
                'signature': base64.b64encode(hmac.new(settings.AWS_SECRET_ACCESS_KEY, policy, hashlib.sha1).digest()),
                'successActionStatus': str(SUCCESS_ACTION_STATUS),
                'actionUrl': "http://" + settings.S3_BUCKET + ".s3.amazonaws.com/",
                'bucket': settings.S3_BUCKET,
                'accessKey': settings.AWS_ACCESS_KEY_ID}
        return Response(res)

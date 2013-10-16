Django Single Page Application Boilerplate
=======

Basic framework for serving a single-page application through Django through Django REST Framework with a front-end setup using Sammy.js for routes and Knockout.js and Require.js to structure ViewModels.

Installation
----------

Install the package via `pip`:

    pip install -e ...

Basic Templating and Knockout App Development
---------------------------------------------

The SPA framework provides a base theme that should be extended to utilize the Knockout App Framework.

Here's an example of a custom theme file that extends the provided base theme:

    {% extends "spa_theme/base.html" %}

    {% block js_settings %}
    <script type="text/javascript">
    var _baseAppViewModel = "viewmodels/baseViewModel";
    </script>
    {% endblock %}

    {% block js %}{% endblock %}

The global Javascript variable `_baseAppViewModel` is used to allow you to declare the base Knockout-based ViewModel that will be bound to the page.  The path of this application is assumed to be under the `js/` directory of a staticfiles directory. The defined ViewModel should extend the `viewmodels/appViewModel` provided by the SPA framework.

Here is an example of a basic `baseViewModel`:

    // define a super-class for the application
    // Will use the SPA app as a mixin
    define(["viewmodels/appViewModel",
        "viewmodels/gameViewModel"],
        function(appViewModel) {
            var baseAppSingleton = function() {
                var self = $.extend(this, appViewModel);
            
                self.init = function() {
                
                }
            
                self.init();
            }
        
            return new baseAppSingleton();
        }
    );

Settings
--------

Create a project-specific settings files that extends the common settings file:

* `spa.config.settings`

Also, do so for one or more of the following settings files depending on your environments:

* `spa.config.environments.development`
* `spa.config.environments.staging`
* `spa.config.environments.production`

You'll need to point the SPA Framework toward the base theme for your project using `SPA_BASE_THEME`.  You should also remember to extend variables that are previously defined by SPA configuration files.

Here's a basic common settings file for a project:

    from spa.config.settings import *
    from path import path

    PROJECT_ROOT = path(__file__).abspath().dirname().dirname()

    SPA_BASE_THEME = "my_theme/base.html"

    STATICFILES_DIRS += (
        PROJECT_ROOT / "static",
    )

    TEMPLATE_DIRS += (
        PROJECT_ROOT / "templates",
    )


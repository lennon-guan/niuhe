NIUHE WebApi Framework
======

What's NIUHE
------
NIUHE framework is a simple webapi framework, which based on flask

Why we need NIUHE
------

How to use
------
```
python /path/to/niuhe/codegen/gen_proj.py <PROJECT_NAME> <MODULE_NAME1> (<MODULE_NAME2> ...)
```
After running this command, the following content is generated in your path:
```
<PROJECT_NAME>
 |- run.py  // the entry of the service
 |- run_gevent.py // also the entry, using gevent
 |- config.py // you know it
 |- devrun.sh // a useful script, which will run the server again and again, preventing stop by bug
 |- app
    |- __init__.py // init application object, loading modules
    |- _common // common models, services for all other modules
    |- <MODULE_NAME1>  // your module 1
      |- models
      |- forms
      |- services
      |- views
      | |- __init__.py // scan all the files which ends with "_view.py" in this directory, and load them automaticly
      | |- xxx_view.py // your view class
      |- protos
        |- xxx_proto.py // define your protocol here
```

We define our own route rule:
* the mapped url is like this: 
```
/<MODULE_NAME>/<SLASHES_SPLITED_VIEW_CLASS_NAME>/<METHOD_NAME_WITHOUT_SURFIX>/
```
* for example, if your module name is "api", view class name is "UserProfile", method name is "foobar_GET", the url is:
```
/api/user_profile/foobar/
```


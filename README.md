Use couchbase as Django cache engine
====
    install
        pip install django_couchbase
    
    settings
        
        USE_COUCHBASE = True
        if USE_COUCHBASE:
            CACHES['default']['BACKEND']= 'django_couchbase.memcached.CouchbaseCache'
            CACHES['default']['LOCATION'] = ['127.0.0.1:8091']
            CACHES['default']['OPTIONS'] = {
                                            'bucket': 'bk',
                                            'password': 'password',
                                            'operation_timeout': 20.5,
                                            'gevent_support': False,
                                            'format': 'PICKLE',
                                            'transcoder':myTranscoder,
                                            'admin:pwd': 'admin:password'
                                            }

                                            
                                            
    format: JSON, PICKLE, UTF8, BYTES, AUTO
    
    http://pythonhosted.org/couchbase/api/couchbase.html
    
    
    
If Error with pypy
	File "pypy_module_cpyext_api_2.c", line 47634, in PyPyObject_IsInstance
	File "pypy_module_cpyext_pyobject.c", line 1144, in BaseCpyTypedescr_realize
	File "pypy_objspace_std_objspace.c", line 5175, in allocate_instance__W_ObjectObject
	File "pypy_objspace_std_typeobject.c", line 3939, in W_TypeObject_check_user_subclass

	Need install python-couchbase-cffi
		https://github.com/couchbaselabs/couchbase-python-cffi
	
	
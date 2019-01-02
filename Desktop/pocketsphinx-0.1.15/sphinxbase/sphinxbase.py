# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.11
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.




"""
This documentation was automatically generated using original comments in
Doxygen format. As some C types and data structures cannot be directly mapped
into Python types, some non-trivial type conversion could have place.
Basically a type is replaced with another one that has the closest match, and
sometimes one argument of generated function comprises several arguments of the
original function (usually two).

Functions having error code as the return value and returning effective
value in one of its arguments are transformed so that the effective value is
returned in a regular fashion and run-time exception is being thrown in case of
negative error code.
"""


from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_sphinxbase', [dirname(__file__)])
        except ImportError:
            import _sphinxbase
            return _sphinxbase
        if fp is not None:
            try:
                _mod = imp.load_module('_sphinxbase', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _sphinxbase = swig_import_helper()
    del swig_import_helper
else:
    import _sphinxbase
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


def _swig_setattr_nondynamic_method(set):
    def set_attr(self,name,value):
        if (name == "thisown"): return self.this.own(value)
        if hasattr(self,name) or (name == "this"):
            set(self,name,value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


class Config(object):
    """Proxy of C Config struct"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _sphinxbase.delete_Config
    __del__ = lambda self : None;
    def set_boolean(self, *args):
        """set_boolean(Config self, char const * key, bool val)"""
        return _sphinxbase.Config_set_boolean(self, *args)

    def set_int(self, *args):
        """set_int(Config self, char const * key, int val)"""
        return _sphinxbase.Config_set_int(self, *args)

    def set_float(self, *args):
        """set_float(Config self, char const * key, double val)"""
        return _sphinxbase.Config_set_float(self, *args)

    def set_string(self, *args):
        """set_string(Config self, char const * key, char const * val)"""
        return _sphinxbase.Config_set_string(self, *args)

    def set_string_extra(self, *args):
        """set_string_extra(Config self, char const * key, char const * val)"""
        return _sphinxbase.Config_set_string_extra(self, *args)

    def exists(self, *args):
        """exists(Config self, char const * key) -> bool"""
        return _sphinxbase.Config_exists(self, *args)

    def get_boolean(self, *args):
        """get_boolean(Config self, char const * key) -> bool"""
        return _sphinxbase.Config_get_boolean(self, *args)

    def get_int(self, *args):
        """get_int(Config self, char const * key) -> int"""
        return _sphinxbase.Config_get_int(self, *args)

    def get_float(self, *args):
        """get_float(Config self, char const * key) -> double"""
        return _sphinxbase.Config_get_float(self, *args)

    def get_string(self, *args):
        """get_string(Config self, char const * key) -> char const *"""
        return _sphinxbase.Config_get_string(self, *args)

Config_swigregister = _sphinxbase.Config_swigregister
Config_swigregister(Config)

class FrontEnd(object):
    """Proxy of C FrontEnd struct"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self): 
        """__init__(FrontEnd self) -> FrontEnd"""
        this = _sphinxbase.new_FrontEnd()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _sphinxbase.delete_FrontEnd
    __del__ = lambda self : None;
    def output_size(self):
        """output_size(FrontEnd self) -> int"""
        return _sphinxbase.FrontEnd_output_size(self)

    def process_utt(self, *args):
        """process_utt(FrontEnd self, char * spch, size_t nsamps, mfcc_t *** cep_block) -> int"""
        return _sphinxbase.FrontEnd_process_utt(self, *args)

FrontEnd_swigregister = _sphinxbase.FrontEnd_swigregister
FrontEnd_swigregister(FrontEnd)

class Feature(object):
    """Proxy of C Feature struct"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _sphinxbase.delete_Feature
    __del__ = lambda self : None;
    def __init__(self): 
        """__init__(Feature self) -> Feature"""
        this = _sphinxbase.new_Feature()
        try: self.this.append(this)
        except: self.this = this
Feature_swigregister = _sphinxbase.Feature_swigregister
Feature_swigregister(Feature)

class FsgModel(object):
    """Proxy of C FsgModel struct"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(FsgModel self, char const * name, LogMath logmath, float lw, int n) -> FsgModel
        __init__(FsgModel self, char const * path, LogMath logmath, float lw) -> FsgModel
        """
        this = _sphinxbase.new_FsgModel(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _sphinxbase.delete_FsgModel
    __del__ = lambda self : None;
    def word_id(self, *args):
        """word_id(FsgModel self, char const * word) -> int"""
        return _sphinxbase.FsgModel_word_id(self, *args)

    def word_add(self, *args):
        """word_add(FsgModel self, char const * word) -> int"""
        return _sphinxbase.FsgModel_word_add(self, *args)

    def trans_add(self, *args):
        """trans_add(FsgModel self, int src, int dst, int logp, int wid)"""
        return _sphinxbase.FsgModel_trans_add(self, *args)

    def null_trans_add(self, *args):
        """null_trans_add(FsgModel self, int src, int dst, int logp) -> int"""
        return _sphinxbase.FsgModel_null_trans_add(self, *args)

    def tag_trans_add(self, *args):
        """tag_trans_add(FsgModel self, int src, int dst, int logp, int wid) -> int"""
        return _sphinxbase.FsgModel_tag_trans_add(self, *args)

    def add_silence(self, *args):
        """add_silence(FsgModel self, char const * silword, int state, float silprob) -> int"""
        return _sphinxbase.FsgModel_add_silence(self, *args)

    def add_alt(self, *args):
        """add_alt(FsgModel self, char const * baseword, char const * altword) -> int"""
        return _sphinxbase.FsgModel_add_alt(self, *args)

    def writefile(self, *args):
        """writefile(FsgModel self, char const * path)"""
        return _sphinxbase.FsgModel_writefile(self, *args)

FsgModel_swigregister = _sphinxbase.FsgModel_swigregister
FsgModel_swigregister(FsgModel)

class JsgfRule(object):
    """Proxy of C JsgfRule struct"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self): 
        """__init__(JsgfRule self) -> JsgfRule"""
        this = _sphinxbase.new_JsgfRule()
        try: self.this.append(this)
        except: self.this = this
    def fromIter(*args):
        """fromIter(void * itor) -> JsgfRule"""
        return _sphinxbase.JsgfRule_fromIter(*args)

    fromIter = staticmethod(fromIter)
    def get_name(self):
        """get_name(JsgfRule self) -> char const *"""
        return _sphinxbase.JsgfRule_get_name(self)

    def is_public(self):
        """is_public(JsgfRule self) -> bool"""
        return _sphinxbase.JsgfRule_is_public(self)

    __swig_destroy__ = _sphinxbase.delete_JsgfRule
    __del__ = lambda self : None;
JsgfRule_swigregister = _sphinxbase.JsgfRule_swigregister
JsgfRule_swigregister(JsgfRule)

def JsgfRule_fromIter(*args):
  """JsgfRule_fromIter(void * itor) -> JsgfRule"""
  return _sphinxbase.JsgfRule_fromIter(*args)

class NGramModel(object):
    """Proxy of C NGramModel struct"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def fromIter(*args):
        """fromIter(void * itor) -> NGramModel"""
        return _sphinxbase.NGramModel_fromIter(*args)

    fromIter = staticmethod(fromIter)
    def __init__(self, *args): 
        """
        __init__(NGramModel self, char const * path) -> NGramModel
        __init__(NGramModel self, Config config, LogMath logmath, char const * path) -> NGramModel
        """
        this = _sphinxbase.new_NGramModel(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _sphinxbase.delete_NGramModel
    __del__ = lambda self : None;
    def write(self, *args):
        """write(NGramModel self, char const * path, int ftype)"""
        return _sphinxbase.NGramModel_write(self, *args)

    def str_to_type(self, *args):
        """str_to_type(NGramModel self, char const * str) -> int"""
        return _sphinxbase.NGramModel_str_to_type(self, *args)

    def type_to_str(self, *args):
        """type_to_str(NGramModel self, int type) -> char const *"""
        return _sphinxbase.NGramModel_type_to_str(self, *args)

    def casefold(self, *args):
        """casefold(NGramModel self, int kase)"""
        return _sphinxbase.NGramModel_casefold(self, *args)

    def size(self):
        """size(NGramModel self) -> int"""
        return _sphinxbase.NGramModel_size(self)

    def add_word(self, *args):
        """add_word(NGramModel self, char const * word, float weight) -> int"""
        return _sphinxbase.NGramModel_add_word(self, *args)

    def prob(self, *args):
        """prob(NGramModel self, size_t n) -> int"""
        return _sphinxbase.NGramModel_prob(self, *args)

NGramModel_swigregister = _sphinxbase.NGramModel_swigregister
NGramModel_swigregister(NGramModel)

def NGramModel_fromIter(*args):
  """NGramModel_fromIter(void * itor) -> NGramModel"""
  return _sphinxbase.NGramModel_fromIter(*args)

class LogMath(object):
    """Proxy of C LogMath struct"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self): 
        """__init__(LogMath self) -> LogMath"""
        this = _sphinxbase.new_LogMath()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _sphinxbase.delete_LogMath
    __del__ = lambda self : None;
    def exp(self, *args):
        """exp(LogMath self, int prob) -> double"""
        return _sphinxbase.LogMath_exp(self, *args)

LogMath_swigregister = _sphinxbase.LogMath_swigregister
LogMath_swigregister(LogMath)

class NGramModelSetIterator(object):
    """Proxy of C NGramModelSetIterator struct"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """__init__(NGramModelSetIterator self, void * ptr) -> NGramModelSetIterator"""
        this = _sphinxbase.new_NGramModelSetIterator(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _sphinxbase.delete_NGramModelSetIterator
    __del__ = lambda self : None;
    def next(self):
        """next(NGramModelSetIterator self) -> NGramModel"""
        return _sphinxbase.NGramModelSetIterator_next(self)

    def __next__(self):
        """__next__(NGramModelSetIterator self) -> NGramModel"""
        return _sphinxbase.NGramModelSetIterator___next__(self)

NGramModelSetIterator_swigregister = _sphinxbase.NGramModelSetIterator_swigregister
NGramModelSetIterator_swigregister(NGramModelSetIterator)

class JsgfIterator(object):
    """Proxy of C JsgfIterator struct"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """__init__(JsgfIterator self, void * ptr) -> JsgfIterator"""
        this = _sphinxbase.new_JsgfIterator(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _sphinxbase.delete_JsgfIterator
    __del__ = lambda self : None;
    def next(self):
        """next(JsgfIterator self) -> JsgfRule"""
        return _sphinxbase.JsgfIterator_next(self)

    def __next__(self):
        """__next__(JsgfIterator self) -> JsgfRule"""
        return _sphinxbase.JsgfIterator___next__(self)

JsgfIterator_swigregister = _sphinxbase.JsgfIterator_swigregister
JsgfIterator_swigregister(JsgfIterator)

class NGramModelSet(object):
    """Proxy of C NGramModelSet struct"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __iter__(self):
        """__iter__(NGramModelSet self) -> NGramModelSetIterator"""
        return _sphinxbase.NGramModelSet___iter__(self)

    def __init__(self, *args): 
        """__init__(NGramModelSet self, Config config, LogMath logmath, char const * path) -> NGramModelSet"""
        this = _sphinxbase.new_NGramModelSet(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _sphinxbase.delete_NGramModelSet
    __del__ = lambda self : None;
    def count(self):
        """count(NGramModelSet self) -> int"""
        return _sphinxbase.NGramModelSet_count(self)

    def add(self, *args):
        """add(NGramModelSet self, NGramModel model, char const * name, float weight, bool reuse_widmap) -> NGramModel"""
        return _sphinxbase.NGramModelSet_add(self, *args)

    def select(self, *args):
        """select(NGramModelSet self, char const * name) -> NGramModel"""
        return _sphinxbase.NGramModelSet_select(self, *args)

    def lookup(self, *args):
        """lookup(NGramModelSet self, char const * name) -> NGramModel"""
        return _sphinxbase.NGramModelSet_lookup(self, *args)

    def current(self):
        """current(NGramModelSet self) -> char const *"""
        return _sphinxbase.NGramModelSet_current(self)

NGramModelSet_swigregister = _sphinxbase.NGramModelSet_swigregister
NGramModelSet_swigregister(NGramModelSet)

class Jsgf(object):
    """Proxy of C Jsgf struct"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __iter__(self):
        """__iter__(Jsgf self) -> JsgfIterator"""
        return _sphinxbase.Jsgf___iter__(self)

    def __init__(self, *args): 
        """__init__(Jsgf self, char const * path) -> Jsgf"""
        this = _sphinxbase.new_Jsgf(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _sphinxbase.delete_Jsgf
    __del__ = lambda self : None;
    def get_name(self):
        """get_name(Jsgf self) -> char const *"""
        return _sphinxbase.Jsgf_get_name(self)

    def get_rule(self, *args):
        """get_rule(Jsgf self, char const * name) -> JsgfRule"""
        return _sphinxbase.Jsgf_get_rule(self, *args)

    def build_fsg(self, *args):
        """build_fsg(Jsgf self, JsgfRule rule, LogMath logmath, float lw) -> FsgModel"""
        return _sphinxbase.Jsgf_build_fsg(self, *args)

Jsgf_swigregister = _sphinxbase.Jsgf_swigregister
Jsgf_swigregister(Jsgf)




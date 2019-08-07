from . import MathObject, Math
 
class Set(MathObject):

    def str(self, *args):
        if "nomath" not in args:
            args = args + ("math",)
        if self.name is not None:
            ans=self.name+"=\{"+self.ans+"\}"
        else:
            ans="\{"+self.ans+"\}"
        return ans.str(*args)

    
def _cross_product(arg0, arg1):
        return arg0+"\\times "+arg1

cross_product = Math(_cross_product)

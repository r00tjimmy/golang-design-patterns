#coding=utf-8

user_var = "rooxx"

def auth_required(myfunc):
  def checkuser(self):
    user = user_var
    if user:
      self.user = user_var
      myfunc(self)
    else:
      print 'unknow user'
  return checkuser


class myHandler():
  @auth_required
  def doProcess(self):
    print ('hello, %s' % self.user)


if __name__ == '__main__':
  mh = myHandler()
  mh.doProcess()

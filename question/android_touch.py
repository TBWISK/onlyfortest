# coding:utf-8
#用于数据模拟点击
#ww.android-doc.com/tools/help/MonkeyDevice.html
import time
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice
device = MonkeyRunner.waitForConnection()
# package = "com.tencent.mm"
# activity = "com.tencent.mm.ui.LauncherUI"
# runCom = package+"/"+activity
# device.startActivity(component = runCom)
# device.touch(200,200,device.DOWN_AND_UP) #DOWN 按下测试按钮
# device.touch(700,50,device.DOWN_AND_UP) ##用于进入万能公众号的属性页面
device.touch(500,500,device.DOWN_AND_UP) ##用于进入认证详情
# time.sleep(3)#延迟点击事件
# device.touch(50,50,device.DOWN_AND_UP)
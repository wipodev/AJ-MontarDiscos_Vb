import socket
import win32serviceutil
import win32service
import win32event
import sys
from usb_drive_monitor import detect_usb_drive

class USBDriveMonitorService(win32serviceutil.ServiceFramework):
    _svc_name_ = "USBDriveMonitorService"
    _svc_display_name_ = "USB Drive Monitor Service"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)
        self.is_alive = True

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.is_alive = False

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
            servicemanager.PYS_SERVICE_STARTED,
            (self._svc_name_, ''))
        self.main()

    def main(self):
        while self.is_alive:
            detect_usb_drive()

if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(USBDriveMonitorService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(USBDriveMonitorService)

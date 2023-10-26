import os
import time
import socket
import win32serviceutil
import win32service
import win32event
import sys
from win10toast import ToastNotifier

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

def detect_usb_drive():
    drives = [chr(drive) for drive in range(68, 91)
              if (os.path.exists(f"{chr(drive)}:"))]

    while True:
        remove_shortcut = [
            drive for drive in drives if not os.path.exists(shortcut(drive))]
        if remove_shortcut:
            for drive in remove_shortcut:
                eject_usb_drive(drive)

        new_drives = [chr(drive) for drive in range(68, 91)
                      if (os.path.exists(f"{chr(drive)}:"))]

        added_drives = [drive for drive in new_drives if drive not in drives]
        if added_drives:
            for drive in added_drives:
                create_shortcut_on_desktop(drive)
                print(f"Se ha conectado una unidad USB en la unidad {drive}:")

        removed_drives = [drive for drive in drives if drive not in new_drives]
        if removed_drives:
            for drive in removed_drives:
                remove_shortcut_from_desktop(drive)
                print(f"Se ha retirado una unidad USB en la unidad {drive}")

        drives = new_drives

def create_shortcut_on_desktop(drive: str) -> None:
    os.system(
        f'powershell $WshShell = New-Object -ComObject WScript.Shell;$Shortcut = $WshShell.CreateShortcut("""{shortcut(drive)}""");$Shortcut.TargetPath = """{drive}:""";$Shortcut.Save()')

def remove_shortcut_from_desktop(drive: str) -> None:
    if os.path.exists(shortcut(drive)):
        os.remove(shortcut(drive))

def eject_usb_drive(drive: str) -> None:
    if os.path.exists(f"{drive}:"):
        os.system(
            f'powershell $driveEject = New-Object -comObject Shell.Application; $driveEject.Namespace(17).ParseName("""{drive}:""").InvokeVerb("""Eject""")')
        print("Ya puede retirar el USB")
        toaster = ToastNotifier()
        toaster.show_toast("USB Drive Monitor", f"Ya puede retirar la unidad USB ({drive})", duration=5)

def shortcut(drive: str) -> str:
    return f"{os.environ['USERPROFILE']}\\Desktop\\Disco local USB ({drive}).lnk"

if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(USBDriveMonitorService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(USBDriveMonitorService)

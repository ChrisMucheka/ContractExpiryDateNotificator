; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{7743755E-C1D9-44FC-B39C-082280BE7CE4}
AppName=ContractNotifier
AppVersion=0.0.1
;AppVerName=ContractNotifier 0.0.1
AppPublisher=EnkosiDigital
AppPublisherURL=http://www.enkosidigital.co.za
AppSupportURL=http://www.enkosidigital.co.za
AppUpdatesURL=http://www.enkosidigital.co.za
DefaultDirName={pf}\ContractNotifier
DisableProgramGroupPage=yes
LicenseFile=C:\Users\Fifofa\PycharmProjects\ExploreData\ContractExpiryDateNotificator\build\exe.win32-3.6\terms and condition.txt
OutputDir=C:\Users\Fifofa\PycharmProjects\ExploreData\ContractExpiryDateNotificator\build\exe.win32-3.6\setup
OutputBaseFilename=contract_notifier_setup
SetupIconFile=C:\Users\Fifofa\PycharmProjects\ExploreData\ContractExpiryDateNotificator\favicon.ico
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked; OnlyBelowVersion: 0,6.1

[Files]
Source: "C:\Users\Fifofa\PycharmProjects\ExploreData\ContractExpiryDateNotificator\build\exe.win32-3.6\example.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Fifofa\PycharmProjects\ExploreData\ContractExpiryDateNotificator\build\exe.win32-3.6\python36.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Fifofa\PycharmProjects\ExploreData\ContractExpiryDateNotificator\build\exe.win32-3.6\tcl86t.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Fifofa\PycharmProjects\ExploreData\ContractExpiryDateNotificator\build\exe.win32-3.6\tk86t.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Fifofa\PycharmProjects\ExploreData\ContractExpiryDateNotificator\build\exe.win32-3.6\lib\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\Fifofa\PycharmProjects\ExploreData\ContractExpiryDateNotificator\build\exe.win32-3.6\tcl\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\Fifofa\PycharmProjects\ExploreData\ContractExpiryDateNotificator\build\exe.win32-3.6\tk\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{commonprograms}\ContractNotifier"; Filename: "{app}\example.exe"
Name: "{commondesktop}\ContractNotifier"; Filename: "{app}\example.exe"; Tasks: desktopicon
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\ContractNotifier"; Filename: "{app}\example.exe"; Tasks: quicklaunchicon

[Run]
Filename: "{app}\example.exe"; Description: "{cm:LaunchProgram,ContractNotifier}"; Flags: nowait postinstall skipifsilent

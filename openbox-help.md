.config/openbox/rc.xml
# Keybinds configuration
    <!-- Keybindings for running applications -->
    <keybind key="W-e">
      <action name="Execute">
        <startupnotify>
          <enabled>true</enabled>
          <name>Konqueror</name>
        </startupnotify>
        <command>chromium</command>
      </action>
    </keybind>
    <keybind key="W-Return">
      <action name="Execute">
        <command>xterm</command>
      </action>
    </keybind>
    <keybind key="W-Left">
      <action name="UnmaximizeFull"/>
      <action name="MaximizeVert"/>
      <action name="MoveResizeTo">
        <width>50%</width>
      </action>
      <action name="MoveToEdge"><direction>west</direction></action>
    </keybind>
    <keybind key="W-Right">
      <action name="UnmaximizeFull"/>
      <action name="MaximizeVert"/>
      <action name="MoveResizeTo">
        <width>50%</width>
      </action>
      <action name="MoveToEdge"><direction>east</direction></action>
    </keybind>
# ibus的应用必须有三个环境变量的设定。
    使用ibus输入需要QT_IM_MODULE,XMODIFIERS,GTK_IM_MODULE, 3个环境变量。必须在~/.config/openbox/environment中设定
#xterm 字体设定
XTerm.vt100.locale: true
XTerm.termName: xterm-256color
XTerm.vt100.faceName: Noto Sans Mono:size=8
XTerm.vt100.scaleHeight: 1.0

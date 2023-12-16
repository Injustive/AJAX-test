MAIN_LOGIN_BUTTON_XPATH = ('(//androidx.compose.ui.platform.ComposeView'
                           '[@resource-id="com.ajaxsystems:id/compose_view"])[1]'
                           '/android.view.View/android.view.View/android.widget.Button')

LOGIN_BUTTON_XPATH = ('(//androidx.compose.ui.platform.ComposeView'
                      '[@resource-id="com.ajaxsystems:id/compose_view"])[4]'
                      '/android.view.View/android.view.View')

LOGIN_EMAIL_XPATH = '(//android.widget.EditText[@resource-id="defaultAutomationId"])[1]'

LOGIN_PASSWORD_XPATH = '(//android.widget.EditText[@resource-id="defaultAutomationId"])[2]'

INVALID_DATA_SNACKBAR = '//android.widget.TextView[@resource-id="com.ajaxsystems:id/snackbar_text"]'

MENU_DRAWER_XPATH = '//android.widget.ImageView[@resource-id="com.ajaxsystems:id/menuDrawer"]'

APP_SETTINGS_XPATH = '//android.view.View[@resource-id="com.ajaxsystems:id/settings"]'

LOGOUT_XPATH = ('(//androidx.compose.ui.platform.ComposeView'
                '[@resource-id="com.ajaxsystems:id/compose_view"])[6]'
                '/android.view.View/android.view.View[1]')

BACK_ARROW_XPATH = '//android.widget.ImageButton[@resource-id="com.ajaxsystems:id/back"]'

SIDEBAR_ELEMS_XPATHS = [('//android.view.View[@resource-id="com.ajaxsystems:id/settings"]', 'Settings'),
                        ('//android.view.View[@resource-id="com.ajaxsystems:id/help"]', 'Help'),
                        ('//android.view.View[@resource-id="com.ajaxsystems:id/logs"]', 'Feedback'),
                        ('//android.view.View[@resource-id="com.ajaxsystems:id/addHub"]', 'Add hub')]

SIDEBAR_XPATH = '//androidx.compose.ui.platform.ComposeView[@resource-id="com.ajaxsystems:id/compose_menu"]'

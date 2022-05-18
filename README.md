# rpi_platform

# information about base
https://wiki.seeedstudio.com/Hercules_Dual_15A_6-20V_Motor_Controller/

# Прошивка контролера базы
- подключить внешнее питание
- начать загрузку прошивки
- перезапустить контроллер базы кнопкой reset

# Контроль базы
- Инициализация пинов: **MOTOR.init**()
- Управление скорость и направлением:   **MOTOR.setSpeedDir1**(80, DIRR); ( **MOTOR.setSpeedDir2**(80, DIRR))
- Дополнительная информация содежиться в библиотеке **motordriver_4wd**

# TODO

1) **setup base_controller: write protocol to controll base by UART**
2) write ROS node to controll base

*) write documentation
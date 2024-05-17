clc
clear

m_bp = 110; % g
m_wheel = 20;
m_sbc = 90;
m_dcmotor = 30;
m_fan = 135;
m_battery = 300;
m_pcb = 20;
m_cables = 12; % g

m_total = (m_bp + 4*m_wheel + m_sbc + 4*m_dcmotor + m_fan + m_battery + m_pcb + m_cables) * 10e-3; % kg

g = [0, 0, -9.81]; % m/sn^2

mu = 0.6; % coefficient of static friction between plastic wheel and brick wall

% Given thrust values

fan_thrust_g = 1870; % thrust in grams

%% F_G towards ground

F_G = m_total * g; % gravitational force in N

%% grams to kg

fan_thrust_kg = fan_thrust_g / 1000; % since 1 kg = 1000 grams

F_fan = [fan_thrust_kg * g(3), 0, 0] ;

%% F_R against ground

F_R = [0, 0, mu * -F_fan(1)]; % maximum static frictional force in N

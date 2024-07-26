% Culture of bacteria
close all;
clear all;

% Global variables
global nu mumax Km Ki Kc kinetics

% Model parameters
nu = 0.5e-11;
mumax = 1.4;
Km = 12;
Ki = 3;
Kc = 3e-11;

% Select growth function (uncomment one of the specific growth rate functions)
% kinetics = 'constant';
% kinetics = 'monod';
% kinetics = 'haldane';
kinetics = 'contois';

% Initial, final time, plot interval
t0 = 0;
tf = 20;
Dtplot = 0.1;

% Initial conditions
%ICs = 'case_1';
ICs = 'case_2';
switch ICs
    case 'case_1'
        X = 1.4e11;
        S = 9;
    case 'case_2'
        X = 1.4e11;
        S = 12;
end

x0 = [X; S];  %initial conditions

% Call to ODE solver
method = 'ode23';
% method = 'ode45';
        t = t0:Dtplot:tf;
        options = odeset('RelTol', 1e-3, 'AbsTol', 1e-3, 'Stats', 'on', 'Events', @events);
switch method
    case 'ode45'
        [tout, xout] = ode45(@bacteria_odes, t, x0, options);
    case 'ode15s'   
        [tout, xout] = ode15s(@bacteria_odes, t, x0, options);
    case 'ode23'
        [tout, xout] = ode23(@bacteria_odes, t, x0, options);
    case 'ode113'
        [tout, xout] = ode113(@bacteria_odes, t, x0, options);
    case 'ode23s'
        [tout, xout] = ode23s(@bacteria_odes, t, x0, options);
    otherwise
        error('Unknown solver method');
end


% Plot results
figure(1)
plot(tout, xout(:, 1));
xlabel('t');
ylabel('X(t)');
title('Biomass concentration');

figure(2)
plot(tout, xout(:, 2));
xlabel('t');
ylabel('S(t)');
title('Substrate concentration');

% Events function (optional)
function [value, isterminal, direction] = events(t, x)
    value = 1;    % Placeholder: no event detection
    isterminal = 1; % Placeholder: stop the integration
    direction = 0;  % Placeholder: all directions
end

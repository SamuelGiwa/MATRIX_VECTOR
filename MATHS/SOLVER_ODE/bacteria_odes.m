function xt = bacteria_odes(t, x)
    % Define global variables
    global nu mumax Km Ki Kc kinetics
    
    % Extract the dependent variables
    X = x(1); % Biomass concentration
    S = x(2); % Substrate concentration
    
    % Initialize the growth rate
    mu = 0;
    
    % Determine the growth rate based on the selected kinetics
    switch kinetics
        case 'constant'
            mu = mumax;
        case 'monod'
            mu = mumax * S / (Km + S);
        case 'haldane'
            mu = mumax * S / (Km + S + (S^2) / Ki);
        case 'contois'
            mu = mumax * S / (Kc * X + S);
        otherwise
            error('Unknown kinetics type');
    end
    
    % Compute the ODEs
    phi = mu * X;  % Growth rate
    Xt = phi;      % Time derivative of biomass concentration
    St = -nu * phi; % Time derivative of substrate concentration
    
    % Combine the derivatives into a column vector
    xt = [Xt; St];
end

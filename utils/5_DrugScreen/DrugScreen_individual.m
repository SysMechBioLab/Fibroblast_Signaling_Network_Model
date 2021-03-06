% SNM Drug Screen: Combinatory Perturbations
% 04.21.2020 JR
% Script wraps drugscreen() fcn in order to run using HPC. 
% 
% Edited 05.07.2020 JR: Added input levels using idealized curves (Zeigler
% MB 2020) + Added multiple screens

%% define drugscreen arguments:
% screen type: combinations (string)
screentype = "individual";
% tension level (doubles)
tension_all = [0.1 0.6];
% knock-out or over-expression (strings)
choice_all = ["KO" "OE"];
% input levels: from InputCurve_12_19.m script
peak = 0.6;                     % peak input level for model
[InputCurves,~,inputNode,~,~] = InputCurve_12_19(peak,peak);
t = 2*7*24;                     % time in h
t0_analysis = 168;              % 168 h added as baseline
t_analysis = t+t0_analysis;     % matches InputCurve script
inputs_baseline = InputCurves(:,t0_analysis);
inputs_infarct = InputCurves(:,t_analysis);

inputs_fraction = 1;
inputs_remote = (inputs_fraction*(inputs_infarct-inputs_baseline))+inputs_baseline;
inputs_all = [inputs_remote inputs_infarct];

%% perform drug screens
fprintf("\n<<<<<< Starting Screen: t=%dwks | LVC=%.2f >>>>>>\n",t/7/24,inputs_fraction)
for choice = choice_all
    for sim = 1:length(tension_all)
        inputs = inputs_all(:,sim);
        tension = tension_all(sim);
        act_delta = drugscreen_mixedtypes(screentype,inputs,inputNode,tension,choice);
        % save results
        tensionname = replace(string(tension),".","");
        filename = strcat(screentype,"_tension",tensionname,"_",choice,".mat");
        save(filename, 'act_delta');
    end
end



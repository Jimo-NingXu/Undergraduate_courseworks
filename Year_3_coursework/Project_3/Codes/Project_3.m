%% Question 1
bananas = readtable('bananas.csv');%Read data
origin=unique(bananas.Origin);%create lists of the unique origins
units=unique(bananas.Units);%create lists of the unique units
%% Question 2
%Calculate the mean of the "Price" column of the "bananas" table, grouped by the "Origin" column.
G = groupsummary(bananas,{'Origin'},'mean','Price');  
%% Question 3
ReqOri={'colombia', 'costa_rica', 'dominican_republic', 'honduras', 'jamaica', 'windward_isles','mexico'};
idx = contains(bananas.Origin,ReqOri);%rows of the "bananas" table contain the origins listed in "ReqOri" would be 1.
reqOridata = bananas(idx,:);og=categorical(reqOridata.Origin);%get the desired origins and stores them
boxchart(og,reqOridata.Price,'Notch','on')
ax = gca; c = ax.TickLabelInterpreter;
ax.TickLabelInterpreter = 'None';
hold on
meanPrice = groupsummary(reqOridata.Price,og,'mean');
plot(meanPrice,'-o')%plots the "meanPrice" data
xlabel('Origins');ylabel('Prices');legend(["Price Data","Price Mean"])
%% Question 4
idx1 = contains(bananas.Origin,'colombia');
colombia = bananas(idx1,2:3);%Get the data regarding colombia
df=mode(hours(-diff(colombia.Date)));colombia=table2timetable(colombia);
if isregular(colombia)==0%Deal with missing data
    colombia=retime(colombia,'regular','makima','TimeStep',hours(df));
end
colombia.Price=filloutliers(colombia.Price,'makima','gesd');%Adjust the outliers
[trend, seasonal, residual] = trenddecomp(colombia.Price);
colombia.Price=seasonal+residual;%Contains detrended data
colombia.Price=zscore(colombia.Price);%Date normalization 
PPP=table(colombia.Price);D=trenddecomp(PPP);
D=splitvars(D);D=addvars(D,colombia.Price);
figure
stackedplot(D)
P=fft(colombia.Price);N = length(P);%FFT
T=days(colombia.Date(end)-colombia.Date(1));%The time span
dt=T/N;Fs=1/dt;f=(0:1:(N/2)-1)*Fs/N;period=1./f;
PP=P(1:floor(N/2));% Extraction of the positive frequency
PP(2:end-1)=2*PP(2:end-1); %Negative frequencies merged into positive frequencies
A=abs(PP);%Calculate the amplitude
figure 
plot(period/7,A)%Amplitude-Period diagram
grid on
xlabel('Weeks/Cycle')
ylabel('Amplitude')
xlim([0 T/7])
vars = D.Properties.VariableNames;PE=[];
for i=2:length(vars)-2
    P1=fft(D{:,i} );
    dt=T/N;Fs=1/dt;f=(0:1:(N/2)-1)*Fs/N;period=1./f;
    PP=P1(1:floor(N/2));% Extraction of the positive frequency
    PP(2:end-1)=2*PP(2:end-1); %Negative frequencies merged into positive frequencies
    A=abs(PP);%Calculate the amplitude
    y=findpeaks(A);t=find(A==max(y));PE=[PE,period(t)/7];
end
result = ismember(PE,period/7);k=any(result);
colombia.Week=week(colombia.Date);x = colombia.Week;cftool
%% Question 5
% Extract data for colombia and costa rica
A=contains(bananas.Origin,'colombia');B=contains(bananas.Origin,'costa_rica');
colombia = bananas(A,2:3);costa_rica=bananas(B,2:3);
%Let price data sampled at same time points
[CC,IC,ID]=union(colombia.Date,costa_rica.Date,'stable');
price1_interp = interp1(colombia.Date, colombia.Price, CC, 'makima');
price2_interp = interp1(costa_rica.Date, costa_rica.Price, CC, 'makima');
% Remove the outliers in Prices and delete the corresponding date
X=filloutliers(price1_interp,'makima','gesd');%Adjust the outliers
Y=filloutliers(price2_interp,'makima','gesd');%Adjust the outlier
CL=zscore(X);RI=zscore(Y);%Data normalization
co=corrcoef(CL,RI);%Find the coefficient
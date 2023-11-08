function dzdt = cases_Q2(t,z)
    xf=z(1);yf=z(2);yr=z(3);df=z(4);dr=z(5);
    sf0=16;sr0=13;muf=0.0002;mur = 0.0008;S=[-200,-400];N=[-200,0];
    k = (yr-yf)/(-yr-xf);%slope of the line connecting two animals
    b = yf-k*xf;%The intercept distance of the line connecting two animals
    k1 = (yf-N(2))/(xf-N(1));%slope of the line connecting the fox and N
    b1= yf-k1*xf;%The intercept distance of the line connecting the fox and N
if k*S(1)+b>=S(2) && k*N(1)+b<=N(2) && S(1)>(S(2)-b1)/k1 %Blocked by S
    dzdt(1,1)=(sf0*exp(-muf*df)*(S(1)-xf))/sqrt((S(1)-xf)^2+(S(2)-yf)^2);%The fox's x
    dzdt(2,1)=(sf0*exp(-muf*df)*(S(2)-yf))/sqrt((S(1)-xf)^2+(S(2)-yf)^2);%The fox's y
    dzdt(3,1)=sqrt(1/2)*sr0*exp(-mur*dr);%The rabbit's y
    dzdt(4,1)=sf0*exp(-muf*df);%Travelled distance of the fox
    dzdt(5,1)=sr0*exp(-mur*dr);%Travelled distance of the rabbit
elseif k*S(1)+b>=S(2) && k*N(1)+b<=N(2) && S(1)<=(S(2)-b1)/k1 %Blocked by N
    dzdt(1,1)=0;
    dzdt(2,1)=sf0*exp(-muf*df);
    dzdt(3,1)=sqrt(1/2)*sr0*exp(-mur*dr);
    dzdt(4,1)=sf0*exp(-muf*df);
    dzdt(5,1)=sr0*exp(-mur*dr);
else %Not blocked
    dzdt(1,1)=(sf0*exp(-muf*df)*(-yr-xf))/sqrt((-yr-xf)^2+(yr-yf)^2);
    dzdt(2,1)=(sf0*exp(-muf*df)*(yr-yf))/sqrt((-yr-xf)^2+(yr-yf)^2);
    dzdt(3,1)=sqrt(1/2)*sr0*exp(-mur*dr);
    dzdt(4,1)=sf0*exp(-muf*df);
    dzdt(5,1)=sr0*exp(-mur*dr);
end
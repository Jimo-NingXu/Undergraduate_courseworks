function dzdt = cases_Q1(t,z)
    xf=z(1);yf=z(2);yr=z(3);
    sf0=16;sr0=13;S=[-200,-400];
    k = (yr-yf)/(-yr-xf);
    b = yf-k*xf;
if k*-200+b>=-400 && k*-200+b<=0 && yf<-400
    dzdt(1,1)=(sf0*(S(1)-xf))/sqrt((S(1)-xf)^2+(S(2)-yf)^2);
    dzdt(2,1)=(sf0*(S(2)-yf))/sqrt((S(1)-xf)^2+(S(2)-yf)^2);
    dzdt(3,1)=sqrt(1/2)*sr0;
elseif k*-200+b>=-400 && k*-200+b<=0
    dzdt(1,1)=0;
    dzdt(2,1)=sf0;
    dzdt(3,1)=sqrt(1/2)*sr0;
else
    dzdt(1,1)=(sf0*(-yr-xf))/sqrt((-yr-xf)^2+(yr-yf)^2);
    dzdt(2,1)=(sf0*(yr-yf))/sqrt((-yr-xf)^2+(yr-yf)^2);
    dzdt(3,1)=sqrt(1/2)*sr0;
end

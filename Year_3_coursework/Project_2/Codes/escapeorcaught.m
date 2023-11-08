function [value,isterminal,direction] = escapeorcaught(t,z)
value(1)=(z(1)+z(3))^2+(z(2)-z(3))^2-0.01;%The distance between two animals <=0.1
isterminal(1)= 1;
direction(1) = -1;
value(2)=z(3)-600;%The rabbit reaches the burrow
isterminal(2)= 1;
direction(2)= 1;
end
function [a,b,c,d,e,f,T3] = findT3 ( N ) 
%findT3 returns the smallest cubic taxicab number T3
% findT3 returns the smallest cubic taxicab number 
% with three methods of express T3=a^3+b^3=c^3+d^3=e^3+f^3 
NUM=[];
 %Two integers whose cubic sum is the same as the M would be stored.
while length(NUM)<6
%The number does not have 2 pairs of integer with the cubic sum equal to M.
    T3=N;
    NUM=[];%Delete the previous elements in NUM.
    num=1:floor(N^(1/3));% All positive integer less than N.
    for i=1:length(num)
        for j=1:length(num)
            if (num(i))^3+(num(j))^3==N && i<=j
                NUM=[NUM,num(i),num(j)];
            end
        end
    end
    N=N+1;
end
[a,b,c,d,e,f,T3]=deal(NUM(1),NUM(2),NUM(3),NUM(4),NUM(5),NUM(6),T3);
end
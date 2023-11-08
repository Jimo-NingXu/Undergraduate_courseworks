function [a,b,c,d,M] = CubicTaxicabNum ( N ) 
%CUBICTAXICABNUM returns the smallest cubic taxicab number M 
% CUBICTAXICABNUM returns the smallest cubic taxicab number 
% M=a^3+b^3=c^3+d^3 greater than
% or equal to N
NUM=[]; 
 %Two integers whose cubic sum is the same as the M would be stored.
while length(NUM)<4 
%The number does not have 2 pairs of integer with the cubic sum equal to M.
    M=N;
    NUM=[];%Delete the previous elements in NUM.
    num=1:floor(N^(1/3));% All positive integer less than N.
    for i=1:length(num)
        for j=i:length(num)
            if (num(i))^3+(num(j))^3==N
                NUM=[NUM,num(i),num(j)];
            end
        end
    end
    N=N+1;
end
[a,b,c,d]=deal(NUM(1),NUM(2),NUM(3),NUM(4));
end
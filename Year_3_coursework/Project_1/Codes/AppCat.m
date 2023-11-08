function [p,q] = AppCat(N)
%APPCat Approximates the catalan constant by the rational number p/q
% APPCat Approximates the catalan constant by the rational number
% p /q , among all pairs of positive integers (p , q ) such that p +q <= N
[Diff,p,catconst]=deal(N,N,0.915965594177219);
q=N-p;
for P=1:N
    for Q=1:N-P  %Make sure p+q<=N
        m=abs(P/Q-catconst); 
        %m records the current difference regarding current P and Q
        if m<Diff || (m==Diff && P+Q<p+q) 
        %Diff stores the smallest difference that ever happened.
            [Diff,p,q]=deal(m,P,Q);
            %p and q store the value corresponding to Diff.
        end
    end
end

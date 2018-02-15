n=100;
p=20;

xi = sign(rand(n,p)-0.5); 

w=zeros(n,n);
for i=1:p
w=w+xi(:,i)*xi(:,i)';
end
for i=1:n
    w(i,i)=0; 
end 
w=w/n;

s=xi(:,1);
%sp=sign(w*s);
%for i=1:20
    sp=s; 
    for j=1:n
        sp(j)=sign(w(j,:)*sp);
    end 
    ham=sum(s ~= sp)
    s=sp;
%end
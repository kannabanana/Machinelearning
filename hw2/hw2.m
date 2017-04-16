%read in from .csv file
filename = 'usps-4-9-train.csv';
[x,delimiterOut] = importdata(filename);

%last column of contains two classes (0 = 4, 1 = 9);
y = x(:,end);
x(:,end) = [];

n = 256;	%number of features
m  = 700;

%w= ((transpose(x)*x)^-1)*transpose(x)*y;
w = zeros(1,700);

n = 256;
m = 700;


newtheta = w;
learning_rate = .01;
for k = 1:n
	the_sum = 0
	for i = 1:m
		the_sum = the_sum + (hypothesis(x(i),w) - y(i))*x(i)(k);
	end
	nudge = the_sum * learning_rate;
	newtheta(k) = newtheta(k)-nudge;
end
w = newtheta;
disp(w);

%read in from .csv file
filename = 'usps-4-9-train.csv';
[x,delimiterOut] = importdata(filename);

%last column of contains two classes (0 = 4, 1 = 9);
y = x(:,end);
x(:,end) = [];

learning_rate = [.2,.02,.002,.0002,.00002,.000002,.000002,.00000002,.00000000000000000000002];

for z=1:9;
	disp(learning_rate(z));
	w = zeros(1,256);
	for i = 1:10000
		delta = zeros(1,256);
		for j=1:1400
			y1 = 1/(1+(exp(-(w)*(transpose(x(j,:))))));
			err = y(j)-y1;
			delta = delta+(err*x(j,:));
		end
		w = w+(learning_rate(z)*delta);
	end
	disp(w);
end


%{
filename = 'usps-4-9-test.csv';
[x,delimiterOut] = importdata(filename);
y = x(:,end);
x(:,end) = [];


%use the same w
for j=1:800
	y1 = 1/(1+(exp(-(w)*(transpose(x(j,:))))));
	err = y(j)-y1;
	disp(err);
end
%}

%read in from .csv file
filename = 'usps-4-9-train.csv';
[x,delimiterOut] = importdata(filename);

%last column of contains two classes (0 = 4, 1 = 9);
y = x(:,end);
x(:,end) = [];



learning_rate = .0000001;
lambda = [.001,.01,.1,1,10,100,1000];
w = zeros(1,256);

for z=1:7
	for i = 1:10000
		delta = zeros(1,256);
		for j=1:1400
			y1 = 1/(1+(exp(-(w)*(transpose(x(j,:))))));
			err = y(j)-y1;
			delta = delta+(err*x(j,:));
		end
		w = w+(learning_rate*(delta+lambda(z)));
		str = 'THIS IS NEW LAMBDA';
		disp(str);
		disp(lambda(z));
		disp(w);
	end
end

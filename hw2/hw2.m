%read in from .csv file
filename = 'usps-4-9-train.csv';
[x,delimiterOut] = importdata(filename);

%last column of contains two classes (0 = 4, 1 = 9);
y = x(:,end);
x(:,end) = [];


str = 'Executing part one';
disp(str);
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
	b = ('the w for the learning rate',learning_rate(z),'is ');
	disp(b);
	disp(w);
end

b = 'we have selected .0000001 as our learning rate';
disp(b);

str = 'executing part 2';
disp(str);

%read in from .csv file
filename = 'usps-4-9-train.csv';
[x,delimiterOut] = importdata(filename);

%last column of contains two classes (0 = 4, 1 = 9);
y = x(:,end);
x(:,end) = [];


accuracy = [];
c_train = 0;

learning_rate = .0000001;
w = zeros(1,256);
total = 0;

for i = 1:10000
	delta = zeros(1,256);
	for j=1:1400	

		y1 = 1/(1+(exp(-(w)*(transpose(x(j,:))))));
		zero = 1-y1;
		ratio = y1/zero;

		if (ratio >1)
			prediction = 1;
		else
			prediction = 0;
		end	

		if (prediction == y(j))
			c_train = c_train+1;
		end
		err = y(j)-y1;
		delta = delta+(err*x(j,:));
		total = total+1;
	end
	w = w+(learning_rate*delta);
	ratio = c_train/total;
	accuracy(i) = ratio;
	c_train = 0;
	total = 0;
		%get a new w - update and guess based on this
end

str = 'writing out training accuracy to traindata.csv';
disp(str);
filename = 'traindata.csv';
csvwrite(filename,accuracy);



%read in from .csv file
filename = 'usps-4-9-test.csv';
[x,delimiterOut] = importdata(filename);

%last column of contains two classes (0 = 4, 1 = 9);
y = x(:,end);
x(:,end) = [];


accuracy = [];
c_test = 0;
total = 0;

for i = 1:10000
	delta = zeros(1,256);
	for j=1:800	

		y1 = 1/(1+(exp(-(w)*(transpose(x(j,:))))));
		zero = 1-y1;
		ratio = y1/zero;

		if (ratio >1)
			prediction = 1;
		else
			prediction = 0;
		end	

		if (prediction == y(j))
			c_test = c_test+1;
		end
		err = y(j)-y1;
		delta = delta+(err*x(j,:));
		total = total+1;
	end
	ratio = c_test/total;
	accuracy(i) = ratio;
	c_test = 0;
	total = 0;
end


str = 'writing out testing accuracy to testdata.csv';
disp(str);
filename = 'testdata.csv';
csvwrite(filename,accuracy);

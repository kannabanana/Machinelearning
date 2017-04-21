%read in from .csv file
filename = 'usps-4-9-train.csv';
[x,delimiterOut] = importdata(filename);

%last column of contains two classes (0 = 4, 1 = 9);
y = x(:,end);
x(:,end) = [];


accuracy = [];
error_train = 0;

learning_rate = .0000001;
w = zeros(1,256);

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

		if (prediction ~= y(j))
			error_train = error_train+1;
		end
		err = y(j)-y1;
		delta = delta+(err*x(j,:));

	end
	w = w+(learning_rate*delta);
	accuracy(i) = error_train;
	error_train = 0;
		%get a new w - update and guess based on this
end

filename = 'traindata.xlsx';
xlswrite(filename,accuracy);



%read in from .csv file
filename = 'usps-4-9-test.csv';
[x,delimiterOut] = importdata(filename);

%last column of contains two classes (0 = 4, 1 = 9);
y = x(:,end);
x(:,end) = [];


accuracy = [];
error_test = 0;

learning_rate = .0000001;

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

		if (prediction ~= y(j))
			error_test = error_test+1;
		end
		err = y(j)-y1;
		delta = delta+(err*x(j,:));

	end
	accuracy(i) = error_test;
	error_test = 0;
end


filename = 'testdata.xlsx';
xlswrite(filename,accuracy);

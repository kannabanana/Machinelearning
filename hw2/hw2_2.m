%read in from .csv file
filename = 'usps-4-9-train.csv';
[x,delimiterOut] = importdata(filename);

%last column of contains two classes (0 = 4, 1 = 9);
y = x(:,end);
x(:,end) = [];

%learning_rate = [.2,.02,.002,.0002,.00002,.000002,.000002,.00000002,.00000000000000000000002];


accuracy = [];
right_train = 0;
right_test = 0;
total = 0;

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

		if (prediction == y(j))
			right_train = right_train+1;
		end
		err = y(j)-y1;
		delta = delta+(err*x(j,:));
		total = total+1;

	end
	w = w+(learning_rate*delta);
	accuracy_c = right_train/total;
	accuracy(i) = accuracy_c;
	right_train = 0;
	total = 0;
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
right_train = 0;
right_test = 0;
total = 0;

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

		if (prediction == y(j))
			right_train = right_train+1;
		end
		err = y(j)-y1;
		delta = delta+(err*x(j,:));
		total = total+1;

	end
	w = w+(learning_rate*delta);
	accuracy_c = right_train/total;
	accuracy(i) = accuracy_c;
	right_train = 0;
	total = 0;
		%get a new w - update and guess based on this
end


filename = 'testdata.xlsx';
xlswrite(filename,accuracy);



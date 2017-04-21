filename = 'usps-4-9-train.csv';
[x,delimiterOut] = importdata(filename);
y = x(:,end);
x(:,end) = [];


filename = 'usps-4-9-test.csv';
[x2,delimiterOut] = importdata(filename);
y2 = x2(:,end);
x2(:,end) = [];


accuracy_train = [];
accuracy_test = [];
c_train = 0;
c_test = 0;
total_train = 0
total_test = 0;

learning_rate = .0000001;
w = zeros(1,256);

for i = 1:10000
	delta = zeros(1,256);
	for j=1:1400	

		yhat = 1/(1+(exp(-(w)*(transpose(x(j,:))))));
		zero = 1-yhat;
		ratio = yhat/zero;

		if (ratio >1)
			prediction = 1;
		else
			prediction = 0;
		end	

		if (prediction == y(j))
			c_train = c_train+1;
		end
		err = y(j)-yhat;
		delta = delta+(err*x(j,:));
		total_train = total_train+1;
	end
	for j=1:800

		yhat = 1/(1+(exp(-(w)*(transpose(x2(j,:))))));
		zero = 1-yhat;
		ratio = yhat/zero;

		if (ratio >1)
			prediction = 1;
		else
			prediction = 0;
		end	

		if (prediction == y2(j))
			c_test = c_test+1;
		end
		total_test = total_test+1;
	end

	w = w+(learning_rate*delta);
	ratio = c_train/total_train;
	accuracy_train(i) = ratio;
	
	ratio = c_test/total_test;
	accuracy_test(i) = ratio;

	c_test = 0;
	c_train = 0;
	total_test = 0;
	total_train = 0;
		%get a new w - update and guess based on this
end

filename = 'traindata.csv';
csvwrite(filename,accuracy_train);
filename = 'testdata.csv';
csvwrite(filename,accuracy_test);

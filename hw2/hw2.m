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

b = 'writing to traindata.csv and testdata.csv';
disp(b);

filename = 'traindata.csv';
csvwrite(filename,accuracy_train);
filename = 'testdata.csv';
csvwrite(filename,accuracy_test);


b = 'starting part 4';

accuracy_train = [];
accuracy_test = [];
c_train = 0;
c_test = 0;
total_train = 0
total_test = 0;

learning_rate = .0000001;
w = zeros(1,256);

lambda = [.001,.01,.1,1,10,100];

for z = 1:6
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

		w = w+(learning_rate*(delta+lambda(z)));
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


	if z ==1
		filename = 'lambda1_train.csv';
		csvwrite(filename,accuracy_train);
		filename = 'lambda1_test.csv';
		csvwrite(filename,accuracy_test);


	elseif z ==2
		filename = 'lambda2_train.csv';
		csvwrite(filename,accuracy_train);
		filename = 'lambda2_test.csv';
		csvwrite(filename,accuracy_test);

	elseif z ==3
		filename = 'lambda3_train.csv';
		csvwrite(filename,accuracy_train);
		filename = 'lambda3_test.csv';
		csvwrite(filename,accuracy_test);


	elseif z ==4
		filename = 'lambda4_train.csv';
		csvwrite(filename,accuracy_train);
		filename = 'lambda4_test.csv';
		csvwrite(filename,accuracy_test);

	elseif z ==5
		filename = 'lambda5_train.csv';
		csvwrite(filename,accuracy_train);
		filename = 'lambda5_test.csv';
		csvwrite(filename,accuracy_test);

	else
		filename = 'lambda6_train.csv';
		csvwrite(filename,accuracy_train);
		filename = 'lambda6_test.csv';
		csvwrite(filename,accuracy_test);
	end
end

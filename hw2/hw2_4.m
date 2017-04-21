accuracy = [];
c_train = 0;

learning_rate = .0000001;
w = zeros(1,256);
total = 0;
lambda = [.001,.01,.1,1,10,100];

for z = 1:6
	filename = 'usps-4-9-train.csv';
	[x,delimiterOut] = importdata(filename);
	y = x(:,end);
	x(:,end) = [];


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
		w = w+(learning_rate*(delta*lambda(z)));
		ratio = c_train/total;
		accuracy(i) = ratio;
		c_train = 0;
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

	if z == 1
		filename = 'testdata.xlsx';
		xlswrite(filename,accuracy);
	elseif z == 2
	elseif z == 3
	elseif z == 4
	elseif z == 5
	elseif z == 6
end;

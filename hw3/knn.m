%get the data and normalize
filename = 'knn_train.csv';
[x_train,delimiterOut] = importdata(filename);
y_train = x_train(:,1)
x_train(:,1) = []
x_train = normc(x_train)


filename = 'knn_test.csv';
[x_test,delimiterOut] = importdata(filename);
y_test = x_test(:,1)
x_test(:,1) = []
x_test = normc(x_test)



%find testing error
for x = 1:284	%loop through all the samples of x_test
	total_distance = zeros(248,248)
	temp = zeros(1,248)
	disp temp
	for y = 1:248	%loop through all the samples of x_train
		D = pdist2(x_test(x,:),x_train(y,:))
		temp(1:y) = (D)
	total_distance(x:1) = temp
	temp = zeros(248)
	end
end

%{
%find nearest neighbors and k error
k_error = zeros(52,1)
temp = 0
for k = 1:51:2
	for j = 1:248
		count = 0
		for x = 1:k
			[M,I] = min(total_distance(j,:))
			count = count+(y_train(j,I))
			total_distance(j,I) = 100
		if (count ~= y_test(j,:))
			k_error(k) = temp+1
		end
			temp = 0
		end
	end
	%find top k elements for each index and check what the right y_test value is
	%keep a for error count for a given for loop interval 
end


disp (k_error)

%}

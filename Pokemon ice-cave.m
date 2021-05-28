save puzzle_example.mat
clc;
clear all;


%%
width = 6;
length = 6;

startpoint_row = [1];
startpoint_column = [3, 4];

endpoint_row = [4, 5];
endpoint_column = [8];

rocks_initial = [0, 0];

odds_of_rocks = 0.1;

%% randomly set startpoint & endpoint

size_s_column = max(size(startpoint_column(1, :)));
size_s_row = max(size(startpoint_row(1, :)));
size_e_column = max(size(endpoint_column(1, :)));
size_e_row = max(size(endpoint_row(1, :)));

s_rand_column = randperm(size_s_column) - 1;
s_rand_row = randperm(size_s_row) - 1;
e_rand_column = randperm(size_e_column) - 1;
e_rand_row = randperm(size_e_row) - 1;

startpoint = zeros(1, 2);
endpoint = zeros(1, 2);

startpoint(1, 1) = startpoint_row(1, 1) + s_rand_row(1, 1);
startpoint(1, 2) = startpoint_column(1, 1) + s_rand_column(1, 1);

endpoint(1, 1) = endpoint_row(1, 1) + e_rand_row(1, 1);
endpoint(1, 2) = endpoint_column(1, 1) + e_rand_column(1, 1);

%% map

map = zeros(length + 2, width + 2);
map(1, :) = 1; map(end, :) = 1;
map(:, 1) = 1; map(:, end) = 1;

for i = 1 : max(size(startpoint_column))
    for j = 1 : max(size(startpoint_row))
        map(startpoint_row(1, j), startpoint_column(1, i)) = 1;
    end
end

for i = 1 : max(size(endpoint_column))
    for j = 1 : max(size(endpoint_row))
        map(endpoint_row(1, j), endpoint_column(1, i)) = 1;
    end
end




%% decide horizontal vs vertical

if startpoint(1, 1) ~= 1
    if startpoint(1, 1) ~= length + 2
       horizontal_s = 1;
       vertical_s = 0;
    elseif startpoint(1, 1) == length + 2
        horizontal_s = 0;
        vertical_s = 1;
    end
elseif startpoint(1, 1) == 1
    horizontal_s = 0;
    vertical_s = 1;
end

if endpoint(1, 1) ~= 1
    if endpoint(1, 1) ~= length + 2
       horizontal_e = 1;
       vertical_e = 0;
    elseif endpoint(1, 1) == length + 2
        horizontal_e = 0;
        vertical_e = 1;
    end
elseif endpoint(1, 1) == 1
    horizontal_e = 0;
    vertical_e = 1;  
end

%% generate path
%% set up
keep = 1;

row = startpoint(1, 1);
column = startpoint(1, 2);

path = zeros(2, 2);  % record path
path(1, 1 : 2) = startpoint;
num_path = 2;

rocks = zeros(1, 2); % record rocks
num_rocks = 1;
if rocks_initial(1, 1) ~= 0
for i = 1 : max(size(rocks_initial(:, 1)))
    rocks(num_rocks, :) = rocks_initial(i, :);
    map(rocks_initial(i, 1), rocks_initial(i, 2)) = 1;
    num_rocks = num_rocks + 1;
end
end

horizontal = horizontal_s;
vertical = vertical_s;


%% paths

while keep == 1


if horizontal == 0
    clearvars column_new;
    clearvars row_new;
     %%% see if rock exists in the same column
    clearvars a; clearvars b;
    if num_path == 2
        map_now = map(:, startpoint(1, 2));

    elseif num_path > 2
        map_now = map(:, path(num_path - 1, 2)); % slice the row we're checking
    end
    map_num = zeros(max(size(map_now)), 1);
    for i = 1 : max(size(map_now))
        map_num(i, 1) = i;
                                                                            disp(map_now)
        
    end
    map_check = zeros(max(size(map_now)), 1);

    for i = 1 : max(size(map_now))
        map_check(i, 1) = map_now(i, 1) * (map_num(i, 1) - path(num_path - 1, 1));
    end %%% 'checker' is set
                                                                            disp(map_check)
    if num_path == 2
        map_check(1, 1) = -1;
    end
                                                                            disp(map_check)
    for i = 1 : max(size(map_now))
        if map_check(i, 1) < 0 %%% check rock
            a = i;
            if map_check(i, 1) < 100 %%% check path
                c = i;
            else
                c = 0;
            end
        elseif map_check(i, 1) > 0 %%% check rock
            b = i;
            if map_check(i, 1) > 100 %%% check path
                d = i;
            else
                d = 0;
            end
        end        
    end
                                                                            disp(a), disp(b), disp(c), disp(d)
%     disp(num_rocks - 1)

if c ~= 0
    a = c + 1;
end
if d ~= 0
    b = d - 1;
end

    rand = randperm(b - a - 1) + a * ones(1, b - a - 1); % x is randomly select, y is fixed
                                                                            disp(b - a - 1)
    
    if rand(1, 1) == row
        row_new = rand(1, 2);
    elseif rand(1, 1) ~= row
        row_new = rand(1, 1);
    end
    
    %%% add path as 100
    for i = min(row, row_new) : max(row, row_new)
        map(i, column) = 100;
    end
        
    
    %%% add rock
    map(row_new + (row_new - row) / abs(row_new - row), column) = 1;
    rocks(num_rocks, :) = [row_new + (row_new - row) / abs(row_new - row), column];
    num_rocks = num_rocks + 1;

    
    %%% update x and y
    path(num_path, 1) = row_new;
    path(num_path, 2) = column;
    

    row = row_new;
    column = column;
    num_path = num_path + 1;
    


    %%% next path = vertical
    horizontal = 1;
    vertical = 0;
    
    if horizontal == horizontal_e
    if row == endpoint(1, 1)
        
    clearvars a; clearvars b;
    map_now = map(path(num_path - 1, 1), :); % slice the row we're checking
    map_num = zeros(1, max(size(map_now)));
    for i = 1 : max(size(map_now))
        map_num(1, i) = i;
    end
    map_check = zeros(1, max(size(map_now)));
    for i = 1 : max(size(map_now))
        map_check(1, i) = map_now(1, i) * (map_num(1, i) - path(num_path - 1, 2));
    end %%% 'checker' is set
    
    for i = 1 : max(size(map_now))
        if map_check(1, i) > 0
            b = i;
        end
    end
    if b == endpoint(1, 2)
        keep = 0;
        
    end
    end
    
        for i = min(row, endpoint(1, 1)) : max(row, endpoint(1, 1))
        for j = min(column, endpoint(1, 2)) : max(column, endpoint(1, 2))
            map(i, j) = 100;
        end
        end
    
    end
    
    
elseif horizontal == 1 %%% have to make new 'column', row is fixed
    %%% see if rock exists in the same row
    clearvars column_new;
    clearvars row_new;
    clearvars a; clearvars b;
    if num_path == 2
        map_now = map(startpoint(1, 1), :);
    elseif num_path > 2
        map_now = map(path(num_path - 1, 1), :); % slice the row we're checking
    end
    map_num = zeros(1, max(size(map_now)));
    for i = 1 : max(size(map_now))
        map_num(1, i) = i;
    end
    map_check = zeros(1, max(size(map_now)));
    for i = 1 : max(size(map_now))
        map_check(1, i) = map_now(1, i) * (map_num(1, i) - path(num_path - 1, 2));
    end %%% 'checker' is set
    
    if num_path == 2
    map_check(1, 1) = -1;
    end
    
    for i = 1 : max(size(map_now))
        if map_check(1, i) < 0 %%% check rock
            a = i;
            if map_check(1, i) < 100 %%% check path
                c = i;
            else
                c = 0;
            end
        elseif map_check(1, i) > 0 %%% check rock
            b = i;
            if map_check(1, i) > 100 %%% check path
                d = i;
            else
                d = 0;
            end
        end        
    end


if c ~= 0
    a = c + 1;
end
if d ~= 0
    b = d - 1;
end

    rand = randperm(b - a - 1) + a * ones(1, b - a - 1); % x is randomly select, y is fixed
                                                                            disp(b - a - 1)    
    if rand(1, 1) == column
        column_new = rand(1, 2);
    elseif rand(1, 1) ~= column
        column_new = rand(1, 1);
    end
    
    %%% add path as 100
    for i = min(column, column_new) : max(column, column_new)
        map(row, i) = 100;
    end
    
    %%% add rock
    map(row, column_new + (column_new - column) / abs(column_new - column)) = 1;
    rocks(num_rocks, :) = [row, column_new + (column_new - column) / abs(column_new - column)];
    num_rocks = num_rocks + 1;
    
    %%% update x and y
    path(num_path, 1) = row;
    path(num_path, 2) = column_new;
    row = row;
    column = column_new;
    num_path = num_path + 1;
    
    %%% next path = horizontal
    horizontal = 0;
    vertical = 1;
    
    %%% stop
    if horizontal == horizontal_e
    if column == endpoint(1, 2)
    clearvars a; clearvars b;
    map_now = map(:, path(num_path - 1, 2)); % slice the row we're checking
    map_num = zeros(max(size(map_now)), 1);
    for i = 1 : max(size(map_now))
        map_num(i, 1) = i;
    end
    map_check = zeros(max(size(map_now)), 1);
    for i = 1 : max(size(map_now))
        map_check(i, 1) = map_now(i, 1) * (map_num(i, 1) - path(num_path - 1, 1));
    end %%% 'checker' is set
    
    for i = 1 : max(size(map_now))
        if map_check(i, 1) > 0
            b = i;
        end
    end
    if b == endpoint(1, 1)
        keep = 0;
    end
    end
    
    for i = min(row, endpoint(1, 1)) : max(row, endpoint(1, 1))
        for j = min(column, endpoint(1, 2)) : max(column, endpoint(1, 2))
            map(i, j) = 100;
        end
    end
    end

end

for i = 1 : 2
    path(num_path, i) = endpoint(1, i);
end
    
end



%% add random rocks
clearvars a;
for i = 1 : width + 2
    for j = 1 : length + 2
        if map(j, i) == 0
            clearvars rand;
            a = rand(1);
            if a < odds_of_rocks
                map(j, i) = 1;
                rocks(num_rocks, :) = [j, i];
                num_rocks = num_rocks + 1;
            end
            clearvars a;
        end
    end
end

num_rocks = num_rocks - 1;
num_path = num_path - 1;
%% generated

map(1, :) = 999999; map(end, :) = 999999;
map(:, 1) = 999999; map(:, end) = 999999;

for i = 1 : max(size(startpoint_column))
    for j = 1 : max(size(startpoint_row))
        map(startpoint_row(1, j), startpoint_column(1, i)) = 1111;
    end
end

for i = 1 : max(size(endpoint_column))
    for j = 1 : max(size(endpoint_row))
        map(endpoint_row(1, j), endpoint_column(1, i)) = 2222;
    end
end

disp(map)
disp(path)


%%
clearvars startpoint_column; clearvars startpoint_row;
clearvars endpoint_column; clearvars endpoint_row;

clearvars s_rand_column; clearvars s_rand_row;
clearvars e_rand_column; clearvars e_rand_row;

%%
% for i = 1 : max(size(path(:, 1)))
%     plot(path(i, 1),path(i, 2),'ro-'); hold on;
%     axis([1, width + 2, 1, length + 2])
% end

plot(path(:, 1),path(:, 2),'ro-'); hold on;
axis([1, width + 2, 1, length + 2])

for i = 1 : max(size(rocks(:, 1)))
    plot(rocks(i, 1),rocks(i, 2),'bo'); hold on;
    axis([1, width + 2, 1, length + 2])
end

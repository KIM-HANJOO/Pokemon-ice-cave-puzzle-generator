save puzzle_example.mat
clc;
clear all;

%%
width = 6;
length = 6;

startpoint_row = [1];
startpoint_column = [3, 4];

endpoint_row = [3, 4];
endpoint_column = [8];

rocks_initial = [3, 4; 5, 6];

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


%% first step
keep = 1;

row = startpoint(1, 1);
column = startpoint(1, 2);
% 
% if horizontal == 0
%     rand_by_width = randperm(width); % x is randomly select, y is fixed
%     if rand_by_width(1, 1) == row
%         row_new = rand_by_width(1, 2);
%     elseif rand_by_width(1, 1) ~= row
%         row_new = rand_by_width(1, 1);
%     end
%     
%     %%% add rock
%     map(row_new + (row_new - row) / abs(row_new - row), column) = 1;
%     rocks(num_rocks, :) = [row_new + (row_new - row) / abs(row_new - row), column];
%     num_rocks = num_rocks + 1;
%     
%     
%     %%% update x and y
%     path(num_path, 1) = row_new;
%     path(num_path, 2) = column;
%     row = row_new;
%     column = column;
%     num_path = num_path + 1;
%     
%     %%% next path = vertical
%     horizontal = 1;
%     vertical = 0;
% 
% elseif horizontal == 1
%     rand_by_length = randperm(length); % x is randomly select, y is fixed
%     if rand_by_length(1, 1) == column
%         column_new = rand_by_length(1, 2);
%     elseif rand_by_length(1, 1) ~= column
%         column_new = rand_by_length(1, 1);
%     end
%     
%     %%% add rock
%     map(row, column_new + (column_new - column) / abs(column_new - column)) = 1;
%     rocks(num_rocks, :) = [row, column_new + (column_new - column) / abs(column_new - column)];
%     num_rocks = num_rocks + 1;
%     
%     %%% update x and y
%     path(num_path, 1) = row;
%     path(num_path, 2) = column_new;
%     row = row;
%     column = column_new;
%     num_path = num_path + 1;
%     
%     %%% next path = horizontal
%     horizontal = 0;
%     vertical = 1;
% end

clearvars rand_by_width;
clearvars rand_by_length;
clearvars row_new;
clearvars column_new;


%% second path, get rid of the possibility that the puzzle can be done immediately
% 
% if horizontal == horizontal_e %%% check the puzzle can be solved immediately
%     if path(2, 1) == endpoint(1, 1) %%% horizontal, same row
%         if endpoint(1, 2) - path(2, 2) > 0 %%% check the path direction
%            rand_col =  randperm(endpoint(1, 2) - path(2, 2) - 2);
%            column_new = rand_col + column; 
%            row = row;
%            
%            %%% add rock
%            rock(row, column_new + 1) = 1;
%            
%         elseif endpoint(1, 2) - path(2, 2) < 0
%            rand_col =  randperm(abs(endpoint(1, 2) - path(2, 2)) - 2);
%            column_new = rand_col - column; 
%            row = row;
%         end
%     end
% end

%% paths after

while keep == 1


if horizontal == 0
    clearvars column_new;
    clearvars row_new;
     %%% see if rock exists in the same column
    a = 1; b = 1;
    if num_path == 2
        map_now = map(:, startpoint(1, 2));
    elseif num_path > 2
        map_now = map(:, path(num_path - 1, 2)); % slice the row we're checking
    end
    map_num = zeros(max(size(map_now)), 1);
    for i = 1 : max(size(map_now))
        map_num(i, 1) = i;
    end
    map_check = zeros(max(size(map_now)), 1);
    for i = 1 : max(size(map_now))
        map_check(i, 1) = map_now(i, 1) * (map_num(i, 1) - path(num_path - 1, 1));
    end %%% 'checker' is set
    
    for i = 1 : max(size(map_now))
        if map_check(i, 1) < 0
            a = i;
        elseif map_check(i, 1) > 0
            b = i;
        end
    end
    
    rand = randperm(b - a - 1) + a * ones(1, b - a - 1); % x is randomly select, y is fixed
        if rand(1, 1) == row
        row_new = rand(1, 2);
    elseif rand(1, 1) ~= row
        row_new = rand(1, 1);
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
        
     a = 1; b = 1;
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
    end
    
    
elseif horizontal == 1 %%% have to make new 'column', row is fixed
    %%% see if rock exists in the same row
    clearvars column_new;
    clearvars row_new;
    a = 1; b = 1;
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
    
    for i = 1 : max(size(map_now))
        if map_check(1, i) < 0
            a = i;
        elseif map_check(1, i) > 0
            b = i;
        end
    end 
    
    
    rand = randperm(b - a - 1) + a * ones(1, b - a - 1); % x is randomly select, y is fixed
    
    if rand(1, 1) == column
        column_new = rand(1, 2);
    elseif rand(1, 1) ~= column
        column_new = rand(1, 1);
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
    
    if horizontal == horizontal_e
    if column == endpoint(1, 2)
    a = 1; b = 1;
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
    end

end

for i = 1 : 2
    path(num_path, i) = endpoint(1, i);
end
    
end
num_rocks = num_rocks - 1;
num_path = num_path - 1;

%% overwrite the walls
map(1, :) = 999999; map(end, :) = 999999;
map(:, 1) = 999999; map(:, end) = 999999;



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
%%
clearvars startpoint_column; clearvars startpoint_row;
clearvars endpoint_column; clearvars endpoint_row;

clearvars s_rand_column; clearvars s_rand_row;
clearvars e_rand_column; clearvars e_rand_row;

%%
plot(path(:, 1),path(:, 2),'ro-'); hold on;
plot(rocks(:, 1), rocks(:, 2), 'bo');
axis([1, width + 2, 1, length + 2])
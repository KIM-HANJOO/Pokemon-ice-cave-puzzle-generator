clc;
clear all;

%%
width = 5;
length = 4;

startpoint_x = [2, 3];
startpoint_y = [0];

endpoint_x = [6];
endpoint_y = [2, 3];

%% randomly set startpoint & endpoint

size_s_x = max(size(startpoint_x(1, :)));
size_s_y = max(size(startpoint_y(1, :)));
size_e_x = max(size(endpoint_x(1, :)));
size_e_y = max(size(endpoint_y(1, :)));

s_rand_x = randperm(size_s_x) - 1;
s_rand_y = randperm(size_s_y) - 1;
e_rand_x = randperm(size_e_x) - 1;
e_rand_y = randperm(size_e_y) - 1;

startpoint = zeros(1, 2);
endpoint = zeros(1, 2);

startpoint(1, 1) = startpoint_x(1, 1) + s_rand_x(1, 1);
startpoint(1, 2) = startpoint_y(1, 1) + s_rand_y(1, 1);

endpoint(1, 1) = endpoint_x(1, 1) + e_rand_x(1, 1);
endpoint(1, 2) = endpoint_y(1, 1) + e_rand_y(1, 1);

clearvars startpoint_x; clearvars startpoint_y;
clearvars endpoint_x; clearvars endpoint_y;

% clearvars size_s_x; clearvars size_s_y;
% clearvars size_e_x; clearvars size_e_y;

clearvars s_rand_x; clearvars s_rand_y;
clearvars e_rand_x; clearvars e_rand_y;

%% generate path (1 means 'yes')

%% decide horizontal vs vertical

if startpoint(1, 1) ~= 0
    if startpoint(1, 1) ~= width + 1
       horizontal_s = 0;
       vertical_s = 1;
    elseif startpoint(1, 1) == width + 1
        horizontal_s = 1;
        vertical_s = 0;
    end
elseif startpoint(1, 1) == 0
    horizontal_s = 1;
    vertical_s = 0;
end

if endpoint(1, 1) ~= 0
    if endpoint(1, 1) ~= length + 1
       horizontal_e = 0;
       vertical_e = 1;
    elseif endpoint(1, 1) == length + 1
        horizontal_e = 1;
        vertical_e = 0;
    end
elseif endpoint(1, 1) == 0
    horizontal_e = 1;
    vertical_e = 0;
end

%%
keep = 1;

x = startpoint(1, 1);
y = startpoint(1, 2);

%% stop point find
% if horizontal_e == 0 % vertical
%     if x == endpoint(1, 1)
%         keep = 0;
%     end
% elseif horizontal_e == 1 % horizontal
%     if y == endpoint(1, 2)
%         keep = 0;
%     end
% end

%% have to add and consider rocks

path = zeros(width * length, 2);
path(1, 1 : 2) = startpoint;
num_path = 2;

rock = zeros(width * length, 2);
num_rock = 1;

horizontal = horizontal_s;
vertical = vertical_s;


while keep == 1
     if horizontal == 0 % vertically move
         %%% choose one
         r_l = randperm(length);
         if r_l(1, 1) == y
             y_r = r_l(1, 2);
         elseif r_l(1, 1) ~= y
             y_r = r_l(1, 1);
         end
         
         %%% horizontal to vertical (vice versa)
         t = horizontal;
         horizontal = vertical;
         vertical = t;
         
         %%% add rock
         rock(num_rock, 1) = x;
         rock(num_rock, 2) = y_r(1, 1) + (y_r(1, 1) - y) / abs(y_r(1, 1) - y);
         num_rock = num_rock + 1;
         
         %%% update x and y
         path(num_path, 1) = x;
         path(num_path, 2) = y_r(1, 1);
         x = x;
         y = y_r(1, 1);
         num_path = num_path + 1;
         
         %%% stop point
         if horizontal_e == 0 % vertical
            if x == endpoint(1, 1)
               keep = 0;
            end
         elseif horizontal_e == 1 % horizontal
            if y == endpoint(1, 2)
               keep = 0;
            end
         end
     end
     
     
     if horizontal == 1 % vertically move
         %%% choose one
         r_w = randperm(width);
         if r_w(1, 1) == x
             x_r = r_w(1, 2);
         elseif r_w(1, 1) ~= x
             x_r = r_w(1, 1);
         end
                  
         %%% horizontal to vertical (vice versa)
         t = horizontal;
         horizontal = vertical;
         vertical = t;
         
         %%% add rock
         rock(num_rock, 1) = x_r(1, 1) + (x_r(1, 1) - x) / abs(x_r(1, 1) - x);
         rock(num_rock, 2) = y;
         num_rock = num_rock + 1;
         
         %%% update x and y
         path(num_path, 1) = x_r(1, 1);
         path(num_path, 2) = y;
         x = x_r(1, 1);
         y = y;
         num_path = num_path + 1;
         
         %%% stop point
         if horizontal_e == 0 % vertical
            if x == endpoint(1, 1)
               keep = 0;
            end
         elseif horizontal_e == 1 % horizontal
            if y == endpoint(1, 2)
               keep = 0;
            end
         end
     end     
end

clearvars x_r; clearvars y_r;



# Thành phần liên thông mạnh

## Sinh viên:

### 22C15019 - NGUYỄN VĂN THẮNG 

### 22C15016 - NGUYỄN HỒNG QUÂN


## Giới thiệu

Thành phần liên thông mạnh(SCC) trong đồ thị là một khái niệm quan trọng trong lý thuyết đồ thị. Thực tế, chúng ta phải giải quyết các bài toán trên đồ thị rất lớn, ví dụ đồ thị kết nối giữa các máy chủ trên Internet hay liên kết giữa các trang web, mạng lưới điện quốc gia hay các kết nối trên một mạng xã hội như Meta. Nếu mỗi thành phần liên thông mạnh được co lại thành một đỉnh, thì đồ thị rất lớn  sẽ trở thành một đồ thị nhỏ hơn. Có nhiều thuật toán để tìm các thành phần liên thông mạnh của một đồ thị cho trước như thuật toán Kosaraju, thuật toán Tarjan và thuật toán Gabow.

## Cài đặt thuật toán tìm SCC (Kosaraju)

Thuật toán Kosaraju được sử dụng để tìm tất cả các thành phần liên thông mạnh trong một đồ thị có hướng. Theo Aho, Hopcroft và Ullman, thuật toán này xuất hiện trong một  bài báo chưa được công bố năm 1978 của S. Rao Kosaraju và Micha Sharir. Thuật toán sử dụng tính chất sau: trong đồ thị chuyển vị (đồ thị trong đó mọi đường đi được đảo ngược so với đồ thị ban đầu, ví dụ: đường đi từ u -> v chuyển thành đường đi từ v -> u) các thành phần liên thông mạnh là không đổi so với đồ thị ban đầu. 

Thuật toán Kosaraju sử dụng hai lần duyệt đồ thị(DFS), một lần duyệt đồ thị gốc và một lần duyệt đồ thị chuyển vị (transpose) của đồ thị gốc. Kết hợp hai lần duyệt này, thuật toán Kosaraju sẽ xác định được tất cả các thành phần liên thông mạnh trong đồ thị.

Cụ thể, các bước của thuật toán Kosaraju như sau: 

- Duyệt đồ thị gốc bằng thuật toán DFS và thêm các đỉnh vào stack theo thứ tự khi thoát khỏi đỉnh.  
- Chuyển vị đồ thị gốc bằng cách đảo ngược các cạnh của đồ thị. 
- Lấy từng đỉnh ra khỏi stack, duyệt đồ thị chuyển vị bằng thuật toán DFS. Mỗi lần duyệt, tạo một thành phần liên thông mạnh mới chứa tất cả các đỉnh được duyệt. 
- Thuật toán sẽ trả về tất cả các thành phần liên thông mạnh của đồ thị.

Mã nguồn: 
```python
def dfs(self, u: Vertex, visited, comp):
    visited.add(u)
    comp.append(u)
    for v in u.getConnections():
        if v not in visited:
            self.dfs(v, visited, comp)


def get_transpose(self):
    gt = Graph()
    for vertex in self:
        gt.addVertex(vertex.getId())
    for vertex in self:
        for neighbor in vertex.getConnections():
            gt.addEdge(neighbor.getId(), vertex.getId(), vertex.getWeight(neighbor))
    return gt


def dfs_order(self, u, stack, visited):
    visited.add(u)
    for v in u.getConnections():
        if v not in visited:
            self.dfs_order(v, stack, visited)
    stack.append(u)


def strongly_connected_components(self):
    stack = []
    visited = set()
    for u in self:
        if u not in visited:
            self.dfs_order(u, stack, visited)
    gt = self.get_transpose()
    visited = set()
    scc = []
    while stack:
        u = gt.getVertex(stack.pop().getId())
        if u not in visited:
            component = []
            gt.dfs(u, visited, component)
            scc.append(component)
    return scc

```

Ta thấy, ở bước xây dựng stack và tạo đồ thị chuyển vị thì đều cần duyệt qua tất cả các đỉnh và cạnh của đồ thị, nên độ phức tạp của 2 bước này đều là O(V+E), trong đó V là số lượng đỉnh của đồ thị và E là số lượng cạnh. Tương tự, sau khi xây dựng được stack, ma trận chuyển vị thì ta duyệt đồ thị một lần nữa để tạo các thành phần liên thông mạnh nên thuật toán Kosaraju sẽ có độ phức tạp O(V+E). Đây là một thuật toán khá hiệu quả trong việc tìm các thành phần liên thông mạnh của đồ thị.

## Ứng dụng thực tế

Giả sử chúng ta có một mạng xã hội với các tài khoản người dùng và các liên kết bạn bè giữa các người dùng. Chúng ta muốn tìm các cộng đồng trong mạng xã hội, nghĩa là các nhóm người dùng mà các thành viên trong nhóm có liên kết bạn bè với nhau nhiều hơn so với các người dùng khác. Để thực hiện điều này, chúng ta có thể sử dụng thuật toán SCC để tìm các thành phần liên thông mạnh trong đồ thị mạng xã hội. Cụ thể, ta có thể xây dựng đồ thị trong đó các nút là các người dùng, và mỗi cạnh giữa hai nút biểu thị một liên kết bạn bè giữa hai người dùng. Sau đó, tìm các thành phần liên thông mạnh trong đồ thị này bằng cách sử dụng thuật toán Kosaraju. 

![](./graph.png)

*Hình 1 Đồ thị mạng xã hội*

Chạy tìm thành phần liên thông cho đồ thị mạng xã hội ở trên:
```python
g = Graph()
for i in range(7):
    g.addVertex(i)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(3, 2)
g.addEdge(3, 4)
g.addEdge(4, 5)
g.addEdge(5, 3)
g.addEdge(6, 5)
scc = g.strongly_connected_components()
for community in scc:
    print([v.getId() for v in community])
```  

Kết quả: 
```
[6]
[3, 5, 4]
[0, 2, 1]
```

Điều này cho thấy rằng trong đồ thị mạng xã hội, có 3 cộng đồng riêng biệt: một cộng đồng bao gồm các người dùng `0, 1 và 2`, và một cộng đồng khác bao gồm các người dùng `3, 4 và 5` và một người dùng riêng biệt là `6`.

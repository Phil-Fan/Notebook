# 链表

## 表的数组实现

查找的时间复杂度 `O(1)`

插入和删除的时间复杂度 `O(N)`

## **单链表**

每一个节点都含有一个表元素和链，该链指向包含该元素后继元的另一个节点，最后一个单元的`next link`指向`nullptr`。

插入和删除操作时间复杂度是 `O(1)`

查询时间复杂度是 `O(N)`

```c++
template <typename DT>
void SingleLinkedList<DT>::insert(DT _val)
{
    if (head == nullptr)
    {
        Node *p = new(Node);
        p->data = _val;
        p->next = nullptr;
        head = p;
        size++;
        currentPosition = head;
    }
    else
    {
        Node *p = new(Node);
        p->data = _val;
        p->next = currentPosition->next;
        currentPosition->next = p;
        size++;
    }
}
```

```c++
template <typename DT>
void SingleLinkedList<DT>::remove()
{
    if (currentPosition == nullptr)
        return;
    if (currentPosition->next == nullptr)
    {
        std::cerr << "Out of Range!" << std::endl;
        std::exit(-1);
    } 
    Node* p = currentPosition->next;
    currentPosition->next = p->next;
    delete p;
    size--;
}
```

## **双链表**

双向链表解决了单向链表 知道删除某一节点但不能获取上一节点的缺点

## **插入操作**

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__DS__assets__01-list.assets__image-20230101164802876.webp)

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__DS__assets__01-list.assets__image-20230101164821049.webp)

## **删除操作**

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__DS__assets__01-list.assets__image-20230101164855945.webp)

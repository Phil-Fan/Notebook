# 以太坊区块链基础

[一文读懂区块链技术](https://blog.chain.link/what-is-blockchain-zh/)

[以太坊基础 - 鹤翔万里的笔记本](https://note.tonycrane.cc/ctf/blockchain/eth/basic/)

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__Web3__assets__blockchain.assets__20240713192452.webp)

两种账户：EOA

有一对公私钥，用于签署交易

- 私钥是随机生成的 256 位数（32 字节）
- 公钥由私钥经过 ECDSA 算法计算而来，是一个 64 字节的数
- 地址由公钥经过 Keccak-256 哈希后取前 20 字节得到

```text
> personal.unlockAccount(eth.accounts[0],"C6HQU#ULHLvv172b")
true
> eth.getBalance(eth.accounts[0])
> eth.sendTransaction({from:eth.accounts[0],to:"0xb3bc02f0b64ab21e34ad594ebc3f1418d6225b85",value:web3.toWei(0.5,"ether"),gas:21000,gasPrice:1000000000},"C6HQU#ULHLvv172b")
> eth.sendTransaction({from:eth.accounts[0],data:"0x608060405234801561001057600080fd5b5060e78061001f6000396000f3fe6080604052348015600f57600080fd5b506004361060285760003560e01c80636d4ce63c14602d575b600080fd5b604080518082018252600b81526a12195b1b1bc815dbdc9b1960aa1b60208201529051605891906061565b60405180910390f35b6000602080835283518082850152825b81811015608b578581018301518582016040015282016071565b81811115609b5783604083870101525b50601f01601f191692909201604001939250505056fea26469706673582212205bfff236f9a503deb7e7a99c401666acaffa5227368cf6855f2aec24e702df2264736f6c63430008030033",gas:200000,gasPrice:1000000000},"=$maE33m&Qx54tpR")

> eth.getTransaction("0x58ba4de9e40c331709954cb10ad80850bb44238944580216ac715d46002fae5f")
> eth.getTransactionReceipt("0x58ba4de9e40c331709954cb10ad80850bb44238944580216ac715d46002fae5f")
```

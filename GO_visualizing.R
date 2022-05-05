#富集结果可视化
library(pheatmap)
library(ggplot2)

#绘制热图
plotfunc = function(term){
  n_term = nrow(term)
  x<-matrix(,2,n_term)
  x[1,] = term$Term
  x[2,] = term$PValue
  for(i in 1:n_term){
    x[2,i] = (-log10(as.numeric(x[2,i])))
  }
  colnames(x) = x[1,]
  x<-as.matrix(x[-1,])
  y<-as.data.frame(lapply(x[,1],as.numeric))
  y<-y[,order(y[1,],decreasing=T)]
  y<-as.matrix(y)
  pheatmap(t(y),cluster_rows = F, cluster_cols = F,color = colorRampPalette(c("White", "LightSalmon","DarkRed"))(50))
}

a <- read.table('D:\\生信\\生物文本挖掘\\GOnew\\GO.xls',sep='\t',header=T)
plotfunc(a)

#绘制气泡图
p = ggplot(a, aes(PValue, Term))
p = p + geom_point()
p = p + geom_point(aes(size=Count))
pbubble = p + geom_point(aes(size=Count, color=-1*log10(PValue)))
pr = pbubble + scale_color_gradient(low='green', high='red')
pr = pr + labs(color=expression(-log[10](PValue)),size='Count', x='PValue', y='Term', title='GO enrichment')
pr + theme_bw()
from rest_framework import serializers

from products.models import Category, Comment, Product


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    comment_text = serializers.CharField(source='text')
    product = serializers.SlugRelatedField(
        slug_field='code', queryset=Product.objects.all()
    )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'comment_text', 'rate', 'product',)


class ProductSerializer(serializers.ModelSerializer):
    avg_rate = serializers.SerializerMethodField()
    category_code = serializers.SlugRelatedField(
        slug_field='code', queryset=Category.objects.all(), source='category'
    )
    comments = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = (
            'name', 'code', 'avg_rate', 'description', 'category_code',
            'quantity', 'pubdate', 'comments',
        )

    def get_avg_rate(self, obj):
        return obj.avg_rate()


class ProductListSerializer(serializers.ModelSerializer):
    avg_rate = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('name', 'code', 'avg_rate',)

    def get_avg_rate(self, obj):
        return obj.avg_rate()


class ProductCreateSerializer(serializers.ModelSerializer):
    category_code = serializers.SlugRelatedField(
        slug_field='code', queryset=Category.objects.all(), source='category'
    )

    class Meta:
        model = Product
        fields = ('name', 'code', 'description', 'category_code', 'quantity',)


class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('name', 'code', 'product_count',)

    def get_product_count(self, obj):
        return obj.count_products()

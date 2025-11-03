from sklearn.neighbors import NearestNeighbors
import numpy as np

class FashionRecommender:
    def __init__(self):
        self.features = None
        self.image_paths = None
        self.knn = None
    
    def build_index(self, features, image_paths):
        self.features = features
        self.image_paths = image_paths
        n_neighbors = min(6, len(features))
        self.knn = NearestNeighbors(n_neighbors=n_neighbors, metric='cosine')
        self.knn.fit(features)
        print(f" Built index with {len(features)} items")
    
    def recommend_similar(self, query_features, n_recommendations=5):
        if self.knn is None:
            raise ValueError("Index not built. Call build_index() first.")
        
        query_features = query_features.reshape(1, -1)
        distances, indices = self.knn.kneighbors(query_features)
        
        recommendations = []
        for i in range(1, min(n_recommendations + 1, len(indices[0]))):
            idx = indices[0][i]
            recommendations.append({
                'image_path': self.image_paths[idx],
                'similarity_score': float(1 - distances[0][i]),
                'index': idx
            })
        return recommendations

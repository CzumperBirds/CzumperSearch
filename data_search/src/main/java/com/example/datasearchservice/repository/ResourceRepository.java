package com.example.datasearchservice.repository;

import com.example.datasearchservice.entity.Resource;
import org.springframework.cache.annotation.CacheConfig;
import org.springframework.data.elasticsearch.repository.ElasticsearchRepository;

import java.util.List;

@CacheConfig(cacheNames = "resources")
public interface ResourceRepository extends ElasticsearchRepository<Resource, String> {
    List<Resource> findByContentContaining(String content);

    List<Resource> findByTagsContaining(List<String> tags);

    List<Resource> findByTagsContainingAndContentContaining(List<String> tags, String content);

    List<Resource> findByTagsContainingOrContentContaining(List<String> tags, String content);
}

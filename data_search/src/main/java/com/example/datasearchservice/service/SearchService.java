package com.example.datasearchservice.service;

import org.elasticsearch.action.search.SearchRequest;
import org.elasticsearch.action.search.SearchResponse;
import com.example.datasearchservice.entity.Resource;
import com.example.datasearchservice.repository.ResourceRepository;
import org.elasticsearch.client.RequestOptions;
import org.elasticsearch.client.RestHighLevelClient;
import org.elasticsearch.search.SearchHits;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.elasticsearch.client.erhlc.RestClients;
import org.springframework.data.elasticsearch.core.ElasticsearchOperations;
import org.springframework.stereotype.Service;
import org.elasticsearch.index.query.BoolQueryBuilder;
import org.elasticsearch.index.query.QueryBuilder;
import org.elasticsearch.index.query.QueryBuilders;
import org.elasticsearch.search.builder.SearchSourceBuilder;


import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

@Service
public class SearchService {
    private final ResourceRepository repository;

    @Autowired
    private ElasticsearchOperations operations;

    public SearchService(ResourceRepository repository) {
        this.repository = repository;
    }
//    public List<Resource> generalSearch(String searchPhrase) {
//        return repository.findByTagsAndContent(Collections.singletonList(searchPhrase), searchPhrase);
//    }
    public List<Resource> searchByContent(String content) {
        return repository.findByContentContaining(content);
    }
    public List<Resource> searchByTags(List<String> tags) {
        return repository.findByTagsContaining(tags);
    }
    public List<Resource> advancedSearch(String content, List<String> tags) throws IOException {

        BoolQueryBuilder boolQueryBuilder = QueryBuilders.boolQuery();
        QueryBuilder queryBuilder = QueryBuilders.matchQuery("content", content);
        QueryBuilder queryBuilder2 = QueryBuilders.termsQuery("tags", tags);
        boolQueryBuilder.should(queryBuilder);
        boolQueryBuilder.should(queryBuilder2);


        operations.search(SearchQuery.queryBuilder().withQuery(boolQueryBuilder).build(), Resource.class);
        SearchResponse searchResponse = client.search(searchRequest, RequestOptions.DEFAULT);
        SearchHits hits = searchResponse.getHits();

        return mapSearchHitsToResources(hits);

    }

    private List<Resource> mapSearchHitsToResources(SearchHits hits) {

        return null;
    }
}

package com.example.datasearchservice.service;

import com.example.datasearchservice.entity.Resource;
import com.example.datasearchservice.repository.ResourceRepository;
import org.springframework.stereotype.Service;

import java.util.Collections;
import java.util.List;
@Service
public class SearchService {
    private final ResourceRepository repository;

    public SearchService(ResourceRepository repository) {
        this.repository = repository;
    }
    public List<Resource> generalSearch(String searchPhrase) {
        return repository.findByTagsContainingAndContentContaining(Collections.singletonList(searchPhrase), searchPhrase);
    }
    public List<Resource> searchByContent(String content) {
        return repository.findByContentContaining(content);
    }
    public List<Resource> searchByTags(List<String> tags) {
        return repository.findByTagsContaining(tags);
    }
    public List<Resource> advancedSearch(String content, List<String> tags) {
        return repository.findByTagsContainingOrContentContaining(tags, content);
    }
}

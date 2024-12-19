package com.example.datasearchservice.api;

import java.util.List;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.example.datasearchservice.entity.Resource;
import com.example.datasearchservice.service.SearchService;

@CrossOrigin(origins = "*")
@RestController
@RequestMapping("/search")
public class SearchController {
    private final SearchService searchService;

    public SearchController(SearchService searchService) {
        this.searchService = searchService;
    }

    @GetMapping
    public List<Resource> generalSearch(@RequestParam String searchPhrase) {
        return searchService.generalSearch(searchPhrase);
    }

    @GetMapping("/content")
    public List<Resource> searchByContent(@RequestParam String searchPhrase) {
        return searchService.searchByContent(searchPhrase);
    }

    @PostMapping("/tags")
    public List<Resource> searchByTags(@RequestBody List<String> searchTags) {
        return searchService.searchByTags(searchTags);
    }

}

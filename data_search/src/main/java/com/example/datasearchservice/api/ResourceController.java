package com.example.datasearchservice.api;

import com.example.datasearchservice.entity.Resource;
import com.example.datasearchservice.repository.ResourceRepository;
import org.springframework.web.bind.annotation.*;
import java.util.Optional;
@RestController
@RequestMapping("/resources")
public class ResourceController {
    private final ResourceRepository repository;
    public ResourceController(ResourceRepository repository) {
        this.repository = repository;
    }
    @PostMapping
    public Resource create(@RequestBody Resource employee) {
        return repository.save(employee);
    }
    @GetMapping("/{id}")
    public Optional<Resource> findById(@PathVariable String id) {
        return repository.findById(id);
    }

    @GetMapping
    public Iterable<Resource> findAll() {
        return repository.findAll();
    }

    @PutMapping("/{id}")
    public Resource update(@PathVariable String id, @RequestBody Resource employee) {
        employee.setId(id);
        return repository.save(employee);
    }

    @DeleteMapping("/{id}")
    public void delete(@PathVariable String id) {
        repository.deleteById(id);
    }
}

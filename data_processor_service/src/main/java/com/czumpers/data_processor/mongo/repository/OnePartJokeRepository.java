package com.czumpers.data_processor.mongo.repository;

import com.czumpers.data_processor.mongo.model.OnePartJokeHash;
import org.springframework.data.mongodb.repository.MongoRepository;

import java.util.Optional;

public interface OnePartJokeRepository extends MongoRepository<OnePartJokeHash, String> {
    Optional<OnePartJokeHash> findByHash(String hash);
}

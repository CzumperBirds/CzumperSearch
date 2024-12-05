package com.czumpers.data_processor.mongo.service;

import com.czumpers.data_processor.kafka.model.OnePartJokeConsumed;
import com.czumpers.data_processor.mongo.model.OnePartJokeHash;
import com.czumpers.data_processor.mongo.repository.OnePartJokeRepository;
import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@AllArgsConstructor
public class OnePartJokeService {
    private final OnePartJokeRepository onePartJokeRepository;

    public boolean isNewJoke(OnePartJokeConsumed joke) {
        String hash = String.valueOf(joke.hashCode());
        return onePartJokeRepository.findByHash(hash).isEmpty();
    }

    public void saveJoke(OnePartJokeConsumed joke) {
        String hash = String.valueOf(joke.hashCode());
        onePartJokeRepository.save(new OnePartJokeHash(hash));
    }
}

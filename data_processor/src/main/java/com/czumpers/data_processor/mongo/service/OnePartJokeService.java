package com.czumpers.data_processor.mongo.service;

import com.czumpers.data_processor.kafka.model.OnePartJokeConsumed;
import com.czumpers.data_processor.mongo.model.OnePartJokeDTO;
import com.czumpers.data_processor.mongo.repository.OnePartJokeRepository;
import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@AllArgsConstructor
public class OnePartJokeService {
    private final OnePartJokeRepository onePartJokeRepository;

    public boolean isNewJoke(OnePartJokeConsumed joke) {
        return onePartJokeRepository.findByJokeId(joke.getId()).isEmpty();
    }

    public void saveJoke(OnePartJokeConsumed joke) {
        onePartJokeRepository.save(new OnePartJokeDTO(joke.getId()));
    }
}

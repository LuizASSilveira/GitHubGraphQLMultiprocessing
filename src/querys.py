
class Query:

    @staticmethod
    def queryRepCommits(after=''):
        query = """query userRepositoryCommit($owner: String!, $name: String!){
                        rateLimit {
                            cost
                            remaining
                            resetAt
                        }
                        repository(owner: $owner, name: $name) {
                            defaultBranchRef {
                                target {
                                    ... on Commit {
                                        history(first:100 $after){
                                            pageInfo{
                                                endCursor,
                                                hasNextPage
                                            }
                                            nodes{
                                                url                    
                                                author{
                                                    user{
                                                        login
                                                    }
                                                }
                                            } 
                                        }
                                    }
                                }
                            }
                        }     
                    }"""
        if after:
            after = ', after: "' + after + '"'
        return query.replace('$after', after)